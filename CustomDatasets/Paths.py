
import os

from . import Utils

# Ensure correct repo placement
Repo = os.path.expanduser("~/DigitalPathology2021/CustomDatasets/")
if not Repo in __file__:
    raise Exception("The repo should be cloned into your home directory!")

# Ensure local img storage is initiatlized
LocalImgsDir = "local_imgs/"
Utils.create_dir(LocalImgsDir)
