#!/usr/bin/env python3
import numpy as np


def map_distances_to_colors(
    distances, 
    clip_max=0.15,
    highlight_range=(0.02, 0.04),
    out_of_range_color=(0.678, 0.847, 0.902) #Light blue
):
    """
    Map distances to RGB colors with smooth transitions:
      - dist < highlight_range[0] → red → green gradient
      - dist in highlight_range → pure green
      - dist > highlight_range[1] → green → blue gradient
      - dist > clip_max → out_of_range_color
    """
    distances = np.abs(distances)
    colors = np.zeros((len(distances), 3))

    low, high = highlight_range

    for i, d in enumerate(distances):
        if d > clip_max:
            colors[i] = out_of_range_color

        elif d < low:
            # Gradient red (1,0,0) → green (0,1,0)
            # t = d / low if low > 0 else 0
            # colors[i] = (1 - t, t, 0)
            # colors[i] = (0.5, 0, 0)
             colors[i] = (1, 0, 0)

        elif d <= high:
            # Pure green
            colors[i] = (0, 1, 0)

        else:
            # Gradient green (0,1,0) → blue (0,0,1)
            colors[i] = (0, 0, 1)

    return colors


def assign_colors(tcloud, clip_max=150, highlight_range=(20, 40)):
    """
    Map the 'distances' field of a tensor PointCloud to 'colors'.
    
    Args:
        tcloud: o3d.t.geometry.PointCloud, must have 'distances' field
        clip_max: maximum distance to clip (values above get out_of_range_color)
        highlight_range: (low, high) range for pure green
    
    Returns:
        tcloud with updated 'colors' field (in-place)
    """
    import open3d as o3d
    if 'distances' not in tcloud.point:
        raise ValueError("PointCloud must have 'distances' field")
    
    distances = tcloud.point['distances'].cpu().numpy()  # CPU numpy array
    colors = map_distances_to_colors(distances, clip_max=clip_max, highlight_range=highlight_range)

    # Update tensor cloud colors
    tcloud.point['colors'] = o3d.core.Tensor(colors.astype(np.float32))
    return tcloud



def surface_area(
    pcd,
    radii=(0.05, 0.07, 0.1),
    estimate_normals=True
) -> float:
    """
    Tính diện tích bề mặt point cloud bằng Ball Pivoting Algorithm (BPA)

    Parameters
    ----------
    pcd : open3d.geometry.PointCloud
        Point cloud đầu vào
    radii : tuple
        Danh sách bán kính ball (nên tăng dần)
    estimate_normals : bool
        Có tự estimate normals hay không

    Returns
    -------
    area : float
        Diện tích bề mặt (đơn vị theo cloud)
    """
    import open3d as o3d
    import copy

    pcd = copy.deepcopy(pcd)

    if isinstance(pcd, o3d.t.geometry.PointCloud):
        pcd = pcd.to_legacy()
    

    pcd = pcd.voxel_down_sample(voxel_size=min(radii) / 2)

    if len(pcd.points) < 20:
        # Quá ít điểm để tính diện tích
        return 0.0

    cl, ind = pcd.remove_radius_outlier(nb_points=8, radius=2*min(radii))
    pcd = pcd.select_by_index(ind)


    if estimate_normals:
        pcd.estimate_normals(
            search_param=o3d.geometry.KDTreeSearchParamHybrid(
                radius=max(radii) * 2,
                max_nn=30
            )
        )
        pcd.orient_normals_consistent_tangent_plane(50)

    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        pcd,
        o3d.utility.DoubleVector(radii)
    )

    # Tính diện tích
    area = mesh.get_surface_area()
    return area



import open3d as o3d


def filter_pcd_by_distance(pcd: o3d.t.geometry.PointCloud,
                           d_min: float,
                           d_max: float) -> o3d.t.geometry.PointCloud:
    """
    Trích xuất point cloud theo trường 'distances'
    
    Parameters
    ----------
    pcd : o3d.t.geometry.PointCloud
        Point cloud tensor đầu vào (phải có field 'distances')
    d_min : float
        Ngưỡng nhỏ nhất
    d_max : float
        Ngưỡng lớn nhất
    
    Returns
    -------
    pcd_out : o3d.t.geometry.PointCloud
        Cloud đã được lọc, giữ nguyên các field khác
    """
    import copy

    if not isinstance(pcd, o3d.t.geometry.PointCloud):
        raise TypeError("Input must be o3d.t.geometry.PointCloud")

    if "distances" not in pcd.point:
        raise KeyError("PointCloud does not contain 'distances' field")

    # Clone để tránh side-effect
    pcd_out = copy.deepcopy(pcd)

    # mask có shape (N, 1) nhưng TensorMap.__getitem__() CHỈ chấp nhận mask dạng (N,)
    distances = pcd_out.point["distances"][:, 0].abs()
    distances_abs = distances.abs()

    # Boolean mask
    mask = (distances_abs >= d_min) & (distances_abs <= d_max)

    # Áp mask cho toàn bộ point attributes
    pcd_out = pcd_out.select_by_mask(mask)

    return pcd_out
