from dataclasses import dataclass, field
from typing import Tuple
import numpy as np
import abc
import uuid
from typing import Dict, Type, Optional


@dataclass
class Shape2D(abc.ABC):
    id: str = field(default_factory=lambda: f"shape_{uuid.uuid4().hex[:8]}")
    type: str = "shape"
    color: str = "yellow"

    # transform (world)
    offset: Tuple[int, int] = (0, 0)

    # cached bbox (world)
    bbox: Tuple[int, int, int, int] = (None, None, None, None)

    # ---------- Transform ----------
    def move_to(self, dx: int, dy: int):
        ox, oy = self.offset
        self.offset = (ox + dx, oy + dy)
        self.update_bbox()


    def set_offset(self, offset: Tuple[int, int]):
        self.offset = offset
        self.update_bbox()

    # ---------- Geometry ----------
    @abc.abstractmethod
    def to_points(self) -> np.ndarray:
        """
        Điểm hình học gốc (local space)
        """
        raise NotImplementedError

    # ---------- World ----------
    def world_points(self) -> np.ndarray:
        ox, oy = self.offset
        return self.to_points() + np.array([ox, oy])


    # ---------- BBox ----------
    def update_bbox(self):
        pts = self.world_points()
        xmin, ymin = pts.min(axis=0)
        xmax, ymax = pts.max(axis=0)

        # self.bbox = (int(xmin), int(ymin), int(xmax), int(ymax))
        self.bbox = (xmin, ymin, xmax, ymax)
        return self.bbox

    # ---------- Hit test ----------
    def contains(self, pos: Tuple[int, int]) -> bool:
        
        if self.bbox[0] is None:
            self.update_bbox()

        x, y = pos
        x1, y1, x2, y2 = self.bbox
        # print('x1, y1, x2, y2',x1, y1, x2, y2, 'self.bbox',self.bbox)
        return x1 <= x <= x2 and y1 <= y <= y2



@dataclass
class Line2D(Shape2D):
    type: str = "line"

    start: Tuple[int, int] = (0, 0)   # local
    end: Tuple[int, int] = (0, 0)
    line_width: float = 1.0

    def to_points(self) -> np.ndarray:
        return np.array([self.start, self.end], dtype=float)


@dataclass
class Text2D(Shape2D):
    type: str = "text"
    text: str = ""
    font_size: float = 11
    line_height: int = 20  # ước lượng height mỗi dòng
    char_width: int = 8    # ước lượng width mỗi ký tự

    def __post_init__(self):
        self.update_bbox()

    def to_points(self) -> np.ndarray:
        """
        Trả về điểm đại diện (local space) cho text.
        Vì text không có line, ta trả về 1 điểm (0,0) → offset sẽ quyết định vị trí
        """
        width = max(len(self.text) * self.char_width, 10)
        height = self.line_height


        # top-left và bottom-right
        return np.array([
            [0, 0],
            [width, height]
        ], dtype=float)

    def update_text(self, new_text: str):
        self.text = new_text
        self.update_bbox()


SHAPE_REGISTRY: Dict[str, Type[Shape2D]] = {
    "line": Line2D,
    "text": Text2D
}


def create_shape(shape_type: str, **kwargs) -> Optional[Shape2D]:
    cls = SHAPE_REGISTRY.get(shape_type.lower())
    if not cls:
        print(f"Unknown shape type: {shape_type}")
        return None
    return cls(**kwargs)

from typing import List, Tuple, Optional

class Shape2DModel:

    def __init__(self):
        self.shapes: List[Shape2D] = []

    def add(self, shape: Shape2D) -> Shape2D:
        for i, s in enumerate(self.shapes):
            if s.id == shape.id:
                # đã tồn tại → replace
                self.shapes[i] = shape
                return shape

        # chưa tồn tại → append
        self.shapes.append(shape)
        return shape

    def remove(self, shape_id):
        """Xóa shape theo id hoặc theo object Shape"""

        if hasattr(shape_id, "id"):
            _id = shape_id.id
        else:
            _id = shape_id

        # modify in-place để không mất reference
        self.shapes[:] = [s for s in self.shapes if s.id != _id]


            

    def get(self, shape_id: str) -> Optional[Shape2D]:
        """Lấy shape theo id"""
        for s in self.shapes:
            if s.id == shape_id:
                return s
        return None

    def all(self) -> List[Shape2D]:
        """Trả về tất cả shape"""
        return list(self.shapes)

    def find_nearest(self, pos: Tuple[int, int]) -> Optional[Shape2D]:
        """Tìm shape chứa vị trí pos gần nhất (ví dụ dùng cho move/select)"""
        best_shape = None
        best_dist = float("inf")
        
        for shape in self.shapes:
            
            if shape.type == 'line':
                if not shape.contains(pos):
                    continue

                # dùng bbox trung tâm để tính khoảng cách
                x1, y1, x2, y2 = shape.bbox
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2

                d = (pos[0] - cx) ** 2 + (pos[1] - cy) ** 2
                if d < best_dist:
                    best_dist = d
                    best_shape = shape
            
            if shape.type == 'text':
                cx, cy = shape.offset

                d = (pos[0] - cx) ** 2 + (pos[1] - cy) ** 2
                if d < best_dist and d < 0.02:
                    best_dist = d
                    best_shape = shape

        return best_shape

    def clear(self):
        """Xóa hết tất cả shape"""
        self.shapes.clear()
