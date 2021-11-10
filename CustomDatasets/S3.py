
# Standard Imports
import os
os.environ['AWS_REGION'] = 'us-east-1'

# NonStandard Imports
import s3fs # https://s3fs.readthedocs.io/en/latest/api.html

# Local Packages
from . import Paths

# S3 Paths
Root = "s3://"
HomeDir = Root + "digpath-data/"
StandardDir = HomeDir + "Standard/"
GlacierDir = HomeDir + "Glacier/"
TestDir = HomeDir + "Test/"

# Simple interface for managing S3 access
class S3Accessor:
    DEFAULT_FORCE = 0
    DEFAULT_RETURN_PATH = False
    def __init__(self):
        self.S3 = s3fs.S3FileSystem(anon=False)
    def file_exists(self, path, on_s3=True):
        if on_s3:
            return self.S3.exists(path)
        else:
            return os.path.exists(path)
    def list_files(self, filepath):
        return self.S3.ls(filepath)
    def get_file(self, s3path, localpath=None, force=DEFAULT_FORCE, return_localpath=DEFAULT_RETURN_PATH):
        if localpath is None: 
            localpath = Paths.LocalImgsDir + os.path.basename(s3path)
        if self.file_exists(localpath, on_s3=False):
            if force == 0: return
            elif force == 1: self.S3.get(s3path, localpath)
            elif force == -1: raise Exception(localpath, "already exists")
        else: self.S3.get(s3path, localpath)
        if return_localpath: return localpath
    def put_file(self, localpath, s3path=None, force=DEFAULT_FORCE, return_s3path=DEFAULT_RETURN_PATH):
        if s3path is None: 
            s3path = Standard + os.path.basename(localpath)
        if self.file_exists(s3path, on_s3=True):
            if force == 0: pass 
            elif force == 1: self.S3.put(localpath, s3path) 
            elif force == -1: raise Exception(s3path, "already exists")
        else: self.S3.put(localpath, s3path)    
        if return_s3path: return s3path
