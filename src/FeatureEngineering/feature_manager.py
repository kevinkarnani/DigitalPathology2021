import importlib
import pyclbr

class FeatureManager():
    '''
    Calculates and returns features based on the features specified in the constructor. 
    If no features are provided automatically calculates all features.

    :param image: A 3 channel image of the cell. 
    :param mask_image: A black and white 3 channel image of the mask of the cell.
    :param features: Optional. A dictionary of features to be calculated.

    Example:
        features = {
            "geometric_features":["Area", "Perimeter"]
        }

    Possible features:
        * geometric_features:
            - Area
            - Perimeter
            - AreaPerimeter
            - InsideRadialContact
    '''
    def __init__(self, image, mask_image, features=None) -> None:
        self.features = features
        self.image = image
        self.mask_image = mask_image
    def __call__(self):
        output = {}
        if not self.features:
            f = pyclbr.readmodule("geometric_features").keys()
            gf = importlib.import_module("geometric_features")
            output["geometric_features"] = {}
            for feature in f:
                c = getattr(gf, feature)
                o = c(mask_image=self.mask_image)
                output["geometric_features"][feature]=o()
            return output
        else:
            for feature_type in self.features.keys():
                gf = importlib.import_module(feature_type)
                output[feature_type] = {}
                for feature in self.features[feature_type]:
                    c = getattr(gf, feature)
                    o = c(mask_image=self.mask_image)
                    output[feature_type][feature] = o()
            return output
            
