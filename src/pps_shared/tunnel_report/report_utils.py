
import numpy as np

class PLYProcessor:
    def __init__(self):
        self.distances = None
        self.pcd = None
        self.target_thickness = 0
        self.tolerance = 0

    def load(self, ply_path):
        import open3d as o3d
        if ply_path is None:
            return None
        try:
            # Kiểm tra nếu là TensorPointCloud
            if isinstance(ply_path, o3d.t.geometry.PointCloud):
                pcd = ply_path
            elif isinstance(ply_path, str):
                pcd = o3d.t.io.read_point_cloud(ply_path)
            else:
                raise TypeError("The cloud not type of TensorPointCloud which have on open3d >= 0.17")
            
            self.pcd = pcd

            if "distances" not in pcd.point:
                raise ValueError("PLY file doesn't contain the [distances] field.")
            self.distances = np.abs(pcd.point["distances"].numpy())
        except Exception as e:
            print(f"Input cloud is not in Open3D Tensor format. {e}")
            return None

        return pcd


    def set_parameters(self, target_thickness, tolerance):
        self.target_thickness = target_thickness
        self.tolerance = tolerance


    def get_header(self):
        header = {
            
        }
        return 


    def export_distribution_chart(self,bins, save_path=None):
        # self.pcd = self.load_ply(self.ply_path)
        img,_,_ = self.__plot_distance_distribution(self.distances, bins, save_path=None)
        return img #image is base64 format for report teamplate html
    

    def export_tunnel_view_image(self, out_path=None):
        
        img_base64 = self.__render_pointcloud_to_image(self.pcd, out_path=out_path)
        return img_base64
    

    def avg_thickness(self):
        if self.distances is None or self.distances.size == 0:
            return None

        min_thickness_mm = max(self.target_thickness - 3 * self.tolerance, 20)

        abs_dist = np.abs(self.distances)
        mask_valid = (abs_dist >= min_thickness_mm)

        valid_ratio = np.mean(mask_valid) * 100  # %

        MIN_VALID_RATIO = 1.0  # % – chỉnh theo yêu cầu kỹ thuật
        if valid_ratio < MIN_VALID_RATIO:
            return 0

        print(f"valid_ratio is {valid_ratio}")
        average_thickness = np.mean(self.distances[mask_valid])
        print(f"average_thickness is {average_thickness}mm")

        return average_thickness
            

    def volume(self):
        """
        Estimate sprayed volume (m³) from distance map.
        Distances are in mm.
        """
        if self.distances is None or self.distances.size == 0:
            return None  # hoặc 0.0 nếu pipeline bắt buộc number

        # minimum valid thickness (mm)
        min_thickness_mm = max(self.target_thickness - 3 * self.tolerance,20)

        # mask valid distances
        abs_dist = np.abs(self.distances)
        mask_valid = (abs_dist >= min_thickness_mm)
        valid_ratio = np.mean(mask_valid) * 100

        MIN_VALID_RATIO = 1.0  # % – chỉnh theo yêu cầu kỹ thuật
        if valid_ratio < MIN_VALID_RATIO:
            return 0  # không đủ dữ liệu để ước tính

        # keep only valid distances
        valid_dist_m = np.zeros_like(self.distances, dtype=float)
        valid_dist_m[mask_valid] = self.distances[mask_valid] / 1000.0  # mm → m

        cell_area = 0.02 * 0.02  # m² per point
        volume_m3 = np.sum(valid_dist_m) * cell_area

        print(f"valid_ratio is {valid_ratio}")
        print(f"volume_m3 is {volume_m3}m3")

        return volume_m3
    
    
    def __plot_distance_distribution(self,distances, bins, save_path=None):
        """
        Plot distance distribution with arbitrary bin edges.
        distances_m: array of distances in meters
        bins_m: list of bin edges in meters (e.g., [0.02, 0.04, 0.06])
        save_path: nếu khác None, lưu hình ảnh ra file (png/jpg/pdf)
        Distances converted to millimeters.
        """
        import numpy as np
        import matplotlib.pyplot as plt
        import io
        import base64

        # Convert to millimeters
        if self.distances is None or len(self.distances) == 0:
            from PIL import Image
            from io import BytesIO

            img = Image.new("RGB", (100, 100), (255, 255, 255))  # RGB trắng hoàn toàn
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

            return f"data:image/png;base64,{img_base64}", 0, 0 
        total = len(distances)

        counts = []
        labels = []

        # < first bin
        counts.append(np.sum(distances < bins[0]))
        labels.append(f"< {bins[0]:.0f} mm")

        # middle bins
        for i in range(len(bins) - 1):
            low, high = bins[i], bins[i + 1]
            counts.append(np.sum((distances >= low) & (distances < high)))
            labels.append(f"[{low:.0f}, {high:.0f}) mm")

        # >= last bin
        counts.append(np.sum(distances >= bins[-1]))
        labels.append(f">= {bins[-1]:.0f} mm")

        # Percentages
        percents = [c / total * 100 for c in counts]

        # 🎨 Màu riêng cho từng cột
        colors = ["#CA150F", "#39EB16", "#09BCF3", "#1120F0", "#C110E0", "#BB00D4"]
        colors = (colors * ((len(labels) // len(colors)) + 1))[:len(labels)]

        # Plot bar chart
        fig, ax = plt.subplots()
        bars = ax.bar(labels, counts, color=colors, edgecolor='none', width=0.2)
        plt.rcParams.update({'font.size': 14})

        # Annotate bars
        for bar, count, pct in zip(bars, counts, percents):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + total * 0.01,
                    f"({pct:.1f}%)",
                    ha='center', va='bottom', fontsize=14)

        ax.set_ylim(0, max(counts) * 1.2)
        ax.set_xlabel("Distance Range (mm)", fontsize=14)
        ax.set_ylabel("Number of Points", fontsize=14)
        ax.set_title("Distance Distribution of Point Cloud", fontsize=14)
        plt.tight_layout()

        # Chuyển figure thành PIL Image
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=150)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        # Lưu hình ảnh nếu save_path khác None
        if save_path:
            fig.savefig(save_path, dpi=300)
            plt.close(fig)  # đóng figure để không hiển thị
        # else:
        #     plt.show()  # nếu không có path thì show bình thường

        return f"data:image/png;base64,{img_base64}", counts, percents 


    def __render_pointcloud_to_image(self, pcd, out_path=None,
                                    width=800, height=600,
                                    fov_deg=55.0,
                                    point_size=2.0,
                                    background=(0.0, 0.0, 0.0)):
        """
        Render a point cloud to image using PyVista (offscreen, Windows-safe).
        Returns base64 PNG string, optionally saves file.
        """

        import io
        import base64
        import numpy as np
        from PIL import Image
        import pyvista as pv

        # ------------------ Extract points + colors ------------------
        if hasattr(pcd, "points"):  # Open3D legacy
            points = np.asarray(pcd.points)
            if points.size == 0:
                raise ValueError("Empty pointcloud")

            if hasattr(pcd, "colors") and len(pcd.colors) == len(points):
                colors = np.asarray(pcd.colors)
                if colors.max() <= 1.0:
                    colors = (colors * 255).astype(np.uint8)
                else:
                    colors = colors.astype(np.uint8)
            else:
                colors = np.full((points.shape[0], 3), 255, dtype=np.uint8)

        elif hasattr(pcd, "point"):  # Open3D tensor
            points = pcd.point["positions"].numpy()
            if points.size == 0:
                raise ValueError("Empty pointcloud")

            if "colors" in pcd.point and pcd.point["colors"].shape[0] == points.shape[0]:
                colors = pcd.point["colors"].numpy()
                if colors.max() <= 1.0:
                    colors = (colors * 255).astype(np.uint8)
                else:
                    colors = colors.astype(np.uint8)
            else:
                colors = np.full((points.shape[0], 3), 255, dtype=np.uint8)

        elif isinstance(pcd, np.ndarray):  # raw numpy
            points = pcd
            colors = np.full((points.shape[0], 3), 255, dtype=np.uint8)

        else:
            raise TypeError("pcd must be Open3D PointCloud or numpy array")

        # ------------------ Create PyVista object ------------------
        cloud = pv.PolyData(points)
        cloud["colors"] = colors

        plotter = pv.Plotter(
            off_screen=True,
            window_size=(width, height)
        )

        plotter.set_background(background)
        plotter.show_axes()
        plotter.add_points(
            cloud,
            scalars="colors",
            rgb=True,
            point_size=float(point_size),
            render_points_as_spheres=False
        )

        # ------------------ Camera auto-fit ------------------
        plotter.camera.view_angle = fov_deg
        # plotter.camera_position = "iso"
        plotter.reset_camera()
        
        center = points.mean(axis=0)
        cam = plotter.camera
        cam.focal_point = center          # nhìn vào tâm cloud
        cam.position = center + np.array([1.0, 0.0, 0.0]) * np.linalg.norm(points.ptp(axis=0))
        cam.up = (0, 0, 1)                 # Z hướng lên
        cam.view_angle = fov_deg


        # ------------------ Render to image ------------------
        img = plotter.screenshot(return_img=True)
        plotter.close()

        # ------------------ Convert to base64 ------------------
        img_pil = Image.fromarray(img)
        buf = io.BytesIO()
        img_pil.save(buf, format="PNG")
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        img_base64_str = f"data:image/png;base64,{img_base64}"

        # ------------------ Save file if requested ------------------
        if out_path:
            img_pil.save(out_path)

        return img_base64_str
