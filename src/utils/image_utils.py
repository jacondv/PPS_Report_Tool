import os
import io
import base64
from PIL import Image
import numpy as np


def image_array_to_base64_png(img: np.ndarray) -> str:
    """
    Convert numpy image array (H×W×C) to base64 PNG data URL string.
    """
    img_pil = Image.fromarray(img)

    buf = io.BytesIO()
    img_pil.save(buf, format="PNG")

    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_base64}"


from PySide6.QtGui import QImage, QPixmap

def image_to_pixmap(image) -> QPixmap | None:
    """
    Convert various image formats to QPixmap.
    Supported:
      - file path (str)
      - PIL.Image.Image
      - base64 string
      - bytes / bytearray
    """

    try:
        # ---------- Case 1: file path ----------
        if isinstance(image, str) and os.path.exists(image):
            return QPixmap(image)

        # ---------- Case 2: base64 string ----------
        if isinstance(image, str):
            if image.startswith("data:"):
                image = image.split(",", 1)[1]

            img_bytes = base64.b64decode(image)
            image = Image.open(io.BytesIO(img_bytes))

        # ---------- Case 3: bytes ----------
        if isinstance(image, (bytes, bytearray)):
            image = Image.open(io.BytesIO(image))

        # ---------- Case 4: PIL Image ----------
        if isinstance(image, Image.Image):
            image = image.convert("RGB")
            w, h = image.size
            data = image.tobytes("raw", "RGB")

            qimg = QImage(
                data,
                w,
                h,
                3 * w,
                QImage.Format.Format_RGB888
            )
            return QPixmap.fromImage(qimg)

    except Exception as e:
        print(f"[to_pixmap] Failed: {e}")

    return None
