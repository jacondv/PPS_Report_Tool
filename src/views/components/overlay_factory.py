import vtk
import math

class OverlayFactory:
    """
    Overlay 2D dùng NormalizedDisplay
    → tự động scale đúng khi screenshot(scale > 1)
    """

    @staticmethod
    def create_polyline(
        points_px,
        plotter_widget,        # (width, height)
        color='yellow',
        closed=False,
        arrow=True,
        line_width=1.0,
        arrow_size_px=12.0
    ):
        if len(points_px) < 2:
            return None

        size = plotter_widget.size()
        w, h = size.width(), size.height()

        # ----------------------------
        # Convert PX -> Normalized
        # ----------------------------
        def norm(p):
            return (p[0] / w, p[1] / h)

        pts_px = [tuple(p) for p in points_px]
        pts = [norm(p) for p in pts_px]

        arrow_size = arrow_size_px / min(w, h)

        vtk_points = vtk.vtkPoints()
        cells_lines = vtk.vtkCellArray()
        cells_polys = vtk.vtkCellArray()

        # ----------------------------
        # Arrow logic (normalized)
        # ----------------------------
        if arrow and len(pts) >= 2:
            p0 = pts[-2]
            p1 = pts[-1]

            dx = p1[0] - p0[0]
            dy = p1[1] - p0[1]
            length = math.hypot(dx, dy)

            if length > 1e-8:
                ux, uy = dx / length, dy / length
                px, py = -uy, ux

                shaft_end = (
                    p1[0] - ux * arrow_size,
                    p1[1] - uy * arrow_size
                )
                pts[-1] = shaft_end

                left = (
                    p1[0] - ux * arrow_size + px * arrow_size * 0.5,
                    p1[1] - uy * arrow_size + py * arrow_size * 0.5
                )
                right = (
                    p1[0] - ux * arrow_size - px * arrow_size * 0.5,
                    p1[1] - uy * arrow_size - py * arrow_size * 0.5
                )
            else:
                return None

        # ----------------------------
        # Insert points
        # ----------------------------
        for p in pts:
            vtk_points.InsertNextPoint(p[0], p[1], 0)

        id_list = list(range(len(pts)))
        if closed:
            id_list.append(0)

        polyline = vtk.vtkPolyLine()
        polyline.GetPointIds().SetNumberOfIds(len(id_list))
        for i, idx in enumerate(id_list):
            polyline.GetPointIds().SetId(i, idx)

        cells_lines.InsertNextCell(polyline)

        if arrow and len(pts) >= 2:
            id_tip = vtk_points.InsertNextPoint(p1[0], p1[1], 0)
            id_l = vtk_points.InsertNextPoint(left[0], left[1], 0)
            id_r = vtk_points.InsertNextPoint(right[0], right[1], 0)

            tri = vtk.vtkTriangle()
            tri.GetPointIds().SetId(0, id_tip)
            tri.GetPointIds().SetId(1, id_l)
            tri.GetPointIds().SetId(2, id_r)
            cells_polys.InsertNextCell(tri)

        # ----------------------------
        # PolyData
        # ----------------------------
        pd = vtk.vtkPolyData()
        pd.SetPoints(vtk_points)
        pd.SetLines(cells_lines)
        pd.SetPolys(cells_polys)

        mapper = vtk.vtkPolyDataMapper2D()
        mapper.SetInputData(pd)

        # 🔴 KEY POINT
        coord = vtk.vtkCoordinate()
        coord.SetCoordinateSystemToNormalizedDisplay()
        mapper.SetTransformCoordinate(coord)

        actor = vtk.vtkActor2D()
        actor.SetMapper(mapper)

        colors = {
            'red': (1, 0, 0),
            'yellow': (1, 1, 0),
            'blue': (0, 0, 1),
            'green': (0, 1, 0),
        }
        actor.GetProperty().SetColor(colors.get(color, (1, 1, 1)))
        actor.GetProperty().SetLineWidth(line_width)

        return actor





