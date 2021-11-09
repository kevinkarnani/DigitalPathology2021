
import os

from . import Utils

# These paths are for local storage
Repo = os.path.expanduser("~/DigitalPathology2021/CustomDatasets/")
#Data = Repo + "data/"
#All = Data + "all.json"
#KFolds = Data + "kfolds/"

# Ensure correct file structure
if not Repo in __file__:
    raise Exception("The repo should be cloned into your home directory!")

# Initialize data dirs
#for path in [Data, KFolds]:
#    utils.create_dir(path)

LocalImgsDir = "/home/sagemaker-user/imgs/"
Utils.create_dir(LocalImgsDir)
