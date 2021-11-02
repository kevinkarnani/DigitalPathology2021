
import io
import os

DEFAULT_SEED = 0

def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)

class FileWrapper(io.IOBase):
    MODE_READ = "r"
    MODE_WRITE = "w"
    VALID_MODES = [MODE_READ, MODE_WRITE]
    def __init__(self, path, mode) -> None:
        self.path = path
        self.mode = mode.lower()
        if self.mode not in FileWrapper.VALID_MODES:
            raise Exception("Yoo r stoopid")
        self.file = None
    def __enter__(self):
        if self.mode == FileWrapper.MODE_READ:
            self.file = open(self.path, "r")
        if self.mode == FileWrapper.MODE_WRITE:
            if os.path.isfile(self.path):
                self.file = open(self.path, "w")
            else:
                self.file = open(self.path, "x")
        return self.file
    def __exit__(self, *args):
        self.file.close()