import vtk
import pyvista as pv

class OverlayFactory:
    """Chuyên tạo các đối tượng đồ họa 2D (Actors)"""
    
    @staticmethod
    def create_polyline(points_2d, color='yellow', closed=False,  **kwargs):
        vtk_points = vtk.vtkPoints()
        line_width = kwargs.get('line_width', 1)
        for p in points_2d:
            vtk_points.InsertNextPoint(p[0], p[1], 0)
        
        # Nếu đóng vùng (Polygon)
        id_list = list(range(len(points_2d)))
        if closed: id_list.append(0)

        polyline = vtk.vtkPolyLine()
        polyline.GetPointIds().SetNumberOfIds(len(id_list))
        for i, idx in enumerate(id_list):
            polyline.GetPointIds().SetId(i, idx)

        cells = vtk.vtkCellArray()
        cells.InsertNextCell(polyline)

        pd = vtk.vtkPolyData()
        pd.SetPoints(vtk_points)
        pd.SetLines(cells)

        mapper = vtk.vtkPolyDataMapper2D()
        mapper.SetInputData(pd)
        
        actor = vtk.vtkActor2D()
        actor.SetMapper(mapper)

        if color == 'red':
            _color = (1.0,0.0,0.0)
        if color == 'yellow':
            _color = (1.0,1.0,0.0)
        if color == 'blue':
            _color = (0.0,0.0,1.0)
        if color == 'green':
            _color = (0.0,1.0,0.0)

        actor.GetProperty().SetColor(_color)
        actor.GetProperty().SetLineWidth(line_width)
        return actor
    