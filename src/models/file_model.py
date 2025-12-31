
import uuid
from pathlib import Path

class FileModel:
    def __init__(self, path: Path):
        self.id = f"file_{uuid.uuid4().hex[:8]}"
        self.path = path
        self.name = path.name
        self.ext = path.suffix.lower()