
import os

import openslide
from PIL import Image
import torch
from torch.utils import data

from . import Paths
from . import S3
from . import Utils

TEST_FILES = ["cat.tiff", "dog.tiff"]

class CustomDataset(data.Dataset):
    def __init__(self, files_dir = S3.Standard, files_filter=None, force_getitem=False, test_files=False):
        # simply stores filenames from S3
        self.S3 = S3.S3Accessor()
        if test_files:
            self.files_dir = S3.Standard
            self.files = TEST_FILES
            self.force_getitem = True
        else:
            self.files_dir = files_dir
            self.files = [os.path.basename(p) for p in self.S3.list_files(self.files_dir)]
            for test_file in TEST_FILES:
                if test_file in self.files: self.files.remove(test_file)
            if files_filter is not None:
                self.files = [f for f in self.files if files_filter(f)]
            self.force_getitem = force_getitem
    def __len__(self):
        return len(self.files)
    def __getitem__(self, index):
        img_path = self.files_dir + self.files[index]
        local_path = self.S3.get_file(img_path, force=self.force_getitem, return_localpath=True)
        img = Image.open(local_path)
        return local_path, openslide.ImageSlide(img)
        
        
        