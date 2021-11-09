
# Standard Imports
import os
os.environ['AWS_REGION'] = 'us-east-1'

# NonStandard Imports
import s3fs

# Local Packages
from . import Paths

# S3 Paths
Root = "s3://"
Dir = Root + "digpath-data/"
Standard = Dir + "Standard/"
Glacier = Dir + "Glacier/"
TestImgs = [Standard+filename for filename in ["dog.png", "cat.png"]]

# Simple interface for managing S3 access
class S3Accessor:
    DEFAULT_FORCE = False
    def __init__(self):
        self.S3 = s3fs.S3FileSystem(anon=False)
    def file_exists(self, path, on_s3=True):
        if on_s3:
            return self.S3.exists(path)
        else:
            return os.path.exists(path)
    def list_files(self, filepath):
        return self.S3.ls(filepath)
    def get_file(self, s3path, localpath=None, force=DEFAULT_FORCE, return_localpath=False):
        if localpath is None: 
            localpath = Paths.LocalImgsDir + os.path.basename(s3path)
        if self.file_exists(localpath, on_s3=False):
            if not force:
                raise Exception(localpath, "already exists")
        self.S3.get(s3path, localpath)
        assert (os.path.exists(localpath)), "ruh roh"
        if return_localpath: return localpath
    def put_file(self, localpath, s3path=None, force=DEFAULT_FORCE, return_s3path=False):
        if s3path is None: 
            s3path = Standard + os.path.basename(localpath)
        if self.file_exists(s3path, on_s3=True):
            if not force: 
                raise Exception(s3path, "already exists")
        self.S3.put(localpath, s3path)    
        if return_s3path: return s3path
