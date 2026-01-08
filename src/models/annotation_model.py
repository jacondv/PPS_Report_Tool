import uuid
from typing import Optional, List, Dict, Tuple
from PIL import ImageFont


class Annotation:
    def __init__(self, msg: str, x: int, y: int, font_size: int = 10, color: str = 'yellow', ann_id: Optional[str] = None):
        if ann_id is None:
            ann_id = f"ann_{uuid.uuid4().hex[:8]}"
        self.id = ann_id
        self.msg = msg
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color

        # width và height khởi tạo = None, tính sau khi gọi update_size()
        self.width = None
        self.height = None


    def update_size(self, font_path: str = "arial.ttf"):
        """
        Tự động tính width/height dựa trên font_size
        và scale phù hợp với GUI viewport
        """
        font = ImageFont.truetype(font_path, self.font_size)
        bbox = font.getbbox(self.msg)  # (x0, y0, x1, y1)

        # width/height gốc
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        # scale tự động theo font_size để phù hợp viewport
        # ước lượng: height ~ font_size, width scale theo tỉ lệ ký tự
        scale_y = self.font_size / h if h != 0 else 1.0
        scale_x = scale_y  # giữ tỷ lệ chữ gốc, có thể tinh chỉnh riêng nếu muốn

        self.width = int(w * scale_x)*2.5
        self.height = int(h * scale_y)*3.5

        return self.width, self.height
    
    def __str__(self):
        return (f"[{self.id}] {self.msg} @ ({self.x}, {self.y}), "
                f"size={self.font_size}, color={self.color}, "
                f"width={self.width}, height={self.height}")

class AnnotationModel:
    """
    Quản lý dữ liệu annotation HUD 2D
    Không phụ thuộc view / plotter
    """
    def __init__(self):
        self.annotations: List[Dict] = []  # list các dict: msg, x, y, font_size, color, id


    def get_by_id(self, ann_id: str) -> Optional[Annotation]:
        """
        Lấy annotation theo id
        """
        for ann in self.annotations:
            if ann.id == ann_id:
                return ann
        return None
    

    def add(self, msg: str, x: int, y: int, font_size: int = 10, color: str = 'yellow', ann_id: Optional[str] = None) -> Annotation:
        ann = Annotation(msg, x, y, font_size, color, ann_id)
        self.annotations.append(ann)
        ann.update_size()
        return ann


    def update(self, ann_id: str, msg: Optional[str] = None, position = None, font_size: Optional[int] = None, color: Optional[str] = None) -> Optional[Annotation]:
        """
        Cập nhật annotation theo id
        - ann_id phải tồn tại, nếu không trả về None
        - Các tham số khác là tùy chọn, chỉ update nếu được truyền
        """
        x,y = None, None
        if position is not None:
            x,y = position

        ann = self.get_by_id(ann_id)
        if ann is None:
            return None  # không tìm thấy, không làm gì

        if msg is not None:
            ann.msg = msg

        if x is not None:
            ann.x = x

        if y is not None:
            ann.y = y

        if color is not None:
            ann.color = color
        
        if font_size is not None:
            ann.font_size = font_size
            ann.update_size()

        return ann


    def update_position(self, ann: 'Annotation', new_x: int, new_y: int):
        """
        Di chuyển annotation
        """
        ann.x = new_x
        ann.y = new_y


    def remove(self, ann_id):
        """
        Xóa annotation khỏi model
        """
        self.annotations = [a for a in self.annotations if a.id != ann_id]


    def find_nearest(self, position: Tuple[int, int]) -> Optional['Annotation']:
        """
        Tìm annotation được click tại position (x, y)
        Nếu click nằm trong bounding box (x,y,width,height) của ann thì chọn ann đó
        Trả về annotation đầu tiên phù hợp, hoặc None nếu không có
        """
        if not (isinstance(position, (tuple, list)) and len(position) == 2 and
                all(isinstance(v, (int, float)) for v in position)):
            raise ValueError("Position must be a tuple/list of 2 numbers (x, y)")

        click_x, click_y = position

        for ann in self.annotations:
            # nếu width/height chưa tính thì tính ngay
            if ann.width is None or ann.height is None:
                ann.update_size()  # tự tính width/height

            # bounding box: ann.x -> ann.x + ann.width, ann.y -> ann.y + ann.height
            if ann.x <= click_x <= 2.5*ann.x + 3.5*ann.width and ann.y <= click_y <= ann.y + ann.height:
                return ann  # click vào vùng này, chọn annotation

        return None  # không có annotation nào được chọn


    def clear(self):
        """
        Xóa tất cả annotation
        """
        self.annotations.clear()
