
#import os

# This is really irritating but is most likely worthwhile
# https://lists.andrew.cmu.edu/pipermail/openslide-users/2014-November/000949.html
#os.add_dll_directory(r'C:\Users\adinb\AppData\Local\Programs\Python\Python39\lib\site-packages\openslide\bin')
import openslide
# https://openslide.org/api/python/

class LazyImage(openslide.ImageSlide):
    def __init__(self, filename) -> None:
        super().__init__()
