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
