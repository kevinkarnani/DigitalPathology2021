
import os
import json

from sklearn.model_selection import KFold

import Paths
import Utils

class CustomDatasetManager:
    def __init__(self) -> None:
        self.__dict__.update(**self.get_all())
        # self.imgs -> [img1.png, img2.png, ...]
        # self.kfolds -> {2:[2.0.json, 2.1.json], ...}
    def get_all(self):
        all = None
        if not os.path.isfile(Paths.All):
            all = {}
            all["imgs"] = [os.path.basename(p) for p in Paths.S3.ls(Paths.Standard) if p.endswith(".tif")]
            all["kfolds"] = {}
        else:
            with utils.FileWrapper(PATH, "r") as f:
                all = json.load(f)
        return all
    def save_all(self):
        with utils.FileWrapper(PATH, "w") as f:
            json.dump(self.__dict__, f)
    def make_kfolds(self, k, files=None, seed=Utils.DEFAULT_SEED):
        if files is None: files = self.imgs
        foldyboi = KFold(k, shuffle=True, random_state=seed)
        kfold_files = []
        for i,(train,test) in enumerate(foldyboi.split(files)):
            train = list(map(lambda i : files[i],train))
            test = list(map(lambda i : files[i],test))
            filename = f"{k}.{i}.json"
            with utils.FileWrapper(Paths.KFolds + filename, "w") as f:
                json.dump({"train":train, "test":test}, f)
            kfold_files.append(filename)
        self.kfolds[k] = kfold_files
        self.save_all()
        return kfold_files
    def get_kfolds(self, k):
        if k not in self.kfolds:
            self.make_k_folds(k)
        return self.kfolds[k] # TODO
