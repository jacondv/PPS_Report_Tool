import vtk
import pyvista as pv
import math

class OverlayFactory:
    """Chuyên tạo các đối tượng đồ họa 2D (Actors)"""
   
    @staticmethod
    def create_polyline(
        points_2d,
        color='yellow',
        closed=False,
        arrow=True,
        **kwargs
    ):
        """
        kwargs:
            line_width: float
            arrow_size: float
        """

        if len(points_2d) < 2:
            return None

        line_width = kwargs.get('line_width', 1.0)
        arrow_size = kwargs.get('arrow_size', 12.0)

        vtk_points = vtk.vtkPoints()
        cells_lines = vtk.vtkCellArray()
        cells_polys = vtk.vtkCellArray()

        # ---- COPY POINTS (SẼ SỬA END NẾU CÓ ARROW) ----
        pts = [tuple(p) for p in points_2d]

        # ---- ARROW LOGIC ----
        if arrow and len(pts) >= 2:
            p0 = pts[-2]
            p1 = pts[-1]

            dx = p1[0] - p0[0]
            dy = p1[1] - p0[1]
            length = math.hypot(dx, dy)

            if length > 1e-6:
                ux, uy = dx / length, dy / length

                # Lùi điểm cuối của line
                offset = arrow_size + line_width * -0.5
                shaft_end = (
                    p1[0] - ux * offset,
                    p1[1] - uy * offset
                )

                pts[-1] = shaft_end

                # Vector vuông góc
                px, py = -uy, ux

                left = (
                    p1[0] - ux * arrow_size + px * arrow_size * 0.5,
                    p1[1] - uy * arrow_size + py * arrow_size * 0.5
                )
                right = (
                    p1[0] - ux * arrow_size - px * arrow_size * 0.5,
                    p1[1] - uy * arrow_size - py * arrow_size * 0.5
                )

        # ---- ADD POINTS TO VTK ----
        for p in pts:
            vtk_points.InsertNextPoint(p[0], p[1], 0)

        # ---- POLYLINE ----
        id_list = list(range(len(pts)))
        if closed:
            id_list.append(0)

        polyline = vtk.vtkPolyLine()
        polyline.GetPointIds().SetNumberOfIds(len(id_list))
        for i, idx in enumerate(id_list):
            polyline.GetPointIds().SetId(i, idx)

        cells_lines.InsertNextCell(polyline)

        # ---- ARROW HEAD (TRIANGLE) ----
        try:
            if arrow and len(pts) >= 2:
                id_tip = vtk_points.InsertNextPoint(p1[0], p1[1], 0)
                id_l = vtk_points.InsertNextPoint(left[0], left[1], 0)
                id_r = vtk_points.InsertNextPoint(right[0], right[1], 0)

                triangle = vtk.vtkTriangle()
                triangle.GetPointIds().SetId(0, id_tip)
                triangle.GetPointIds().SetId(1, id_l)
                triangle.GetPointIds().SetId(2, id_r)

                cells_polys.InsertNextCell(triangle)
        except:
            pass

        # ---- POLYDATA ----
        pd = vtk.vtkPolyData()
        pd.SetPoints(vtk_points)
        pd.SetLines(cells_lines)
        pd.SetPolys(cells_polys)

        mapper = vtk.vtkPolyDataMapper2D()
        mapper.SetInputData(pd)

        actor = vtk.vtkActor2D()
        actor.SetMapper(mapper)

        # ---- COLOR ----
        colors = {
            'red': (1, 0, 0),
            'yellow': (1, 1, 0),
            'blue': (0, 0, 1),
            'green': (0, 1, 0),
        }
        actor.GetProperty().SetColor(colors.get(color, (1, 1, 1)))
        actor.GetProperty().SetLineWidth(line_width)

        return actor
    


 
    # @staticmethod
    # def create_polyline(points_2d, color='yellow', closed=False,  **kwargs):
    #     vtk_points = vtk.vtkPoints()
    #     line_width = kwargs.get('line_width', 1)
    #     for p in points_2d:
    #         vtk_points.InsertNextPoint(p[0], p[1], 0)
        
    #     # Nếu đóng vùng (Polygon)
    #     id_list = list(range(len(points_2d)))
    #     if closed: id_list.append(0)

    #     polyline = vtk.vtkPolyLine()
    #     polyline.GetPointIds().SetNumberOfIds(len(id_list))
    #     for i, idx in enumerate(id_list):
    #         polyline.GetPointIds().SetId(i, idx)

    #     cells = vtk.vtkCellArray()
    #     cells.InsertNextCell(polyline)

    #     pd = vtk.vtkPolyData()
    #     pd.SetPoints(vtk_points)
    #     pd.SetLines(cells)

    #     mapper = vtk.vtkPolyDataMapper2D()
    #     mapper.SetInputData(pd)
        
    #     actor = vtk.vtkActor2D()
    #     actor.SetMapper(mapper)

    #     if color == 'red':
    #         _color = (1.0,0.0,0.0)
    #     if color == 'yellow':
    #         _color = (1.0,1.0,0.0)
    #     if color == 'blue':
    #         _color = (0.0,0.0,1.0)
    #     if color == 'green':
    #         _color = (0.0,1.0,0.0)

    #     actor.GetProperty().SetColor(_color)
    #     actor.GetProperty().SetLineWidth(line_width)
    #     return actor
    