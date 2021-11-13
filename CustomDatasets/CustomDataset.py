
import os

import openslide # https://openslide.org/api/python/
from PIL import Image
import torch
from torch.utils import data # https://pytorch.org/tutorials/beginner/data_loading_tutorial.html

from . import Paths
from . import S3
from . import Utils

DEFAULT_FILES_EXTENSION = ".tif"

class CustomDataset(data.Dataset):
    def __init__(self, files_dir=S3.StandardDir, files_ext=DEFAULT_FILES_EXTENSION, force_getitem=0):
        self.S3 = S3.S3Accessor()
        self.files_dir = files_dir
        self.files_ext = files_ext
        self.files = [os.path.basename(p) for p in self.S3.list_files(self.files_dir) if p.endswith(self.files_ext)]
        self.force_getitem = force_getitem # force_getitem : (0, don't overwrite existing file), (1, overwrite if file exists), (-1, throw error if file already exists locally)
    def __len__(self):
        return len(self.files)
    def __getitem__(self, index):
        s3img_path = self.files_dir + self.files[index]
        local_path = self.S3.get_file(s3img_path, force=self.force_getitem, return_localpath=True)
        img = self.make_openslide_img(local_path)
        return local_path, img
    def make_openslide_img(self, local_path):
        assert (os.path.exists(local_path)), f"{local_path} doesn't exist"
        img = openslide.OpenSlide(local_path)
        return img
    def get_img_by_name(self, name):
        index = self.files.index(name)
        return self[index]
    def delete_cache(self):
        self.S3.delete_cache(self.files_dir, self.files_ext)
        
class TestDataset(CustomDataset):
    def __init__(self, configuration=0):
        if configuration == 0:
            super().__init__(files_dir=S3.TestDir, force_getitem=0)
        elif configuration == 1:
            super().__init__(files_dir=S3.StandardDir, force_getitem=1)
            self.files = ["84278T_001.tif"] # this file is only 1.1 GB
    def make_openslide_img(self, local_path):
        assert (os.path.exists(local_path)), f"{local_path} doesn't exist"
        img = Image.open(local_path)
        img = openslide.ImageSlide(img)
        return img
        