import feature
from matplotlib.colors import rgb_to_hsv
from numpy import mean
from numpy.ma import masked_array

class MeanHSV(feature.Feature):
    '''
    Uses the mask to calculate the mean of HSV channels only for the cell pixels. 
    
    :param image: 3 Channel image of the cell.
    :param mask_image: 3 Channel image of the mask.
    :returns: A list with mean values of H, S, and V channels respectively.
    '''
    def _calculate_feature(self):
        hsv = rgb_to_hsv(self.image)
        masked1 = masked_array(hsv[:, :, 0], self.bin_mask)
        masked2 = masked_array(hsv[:, :, 1], self.bin_mask)
        masked3 = masked_array(hsv[:,:,2], self.bin_mask)
        return [masked1.mean(), masked2.mean(), masked3.mean()]
