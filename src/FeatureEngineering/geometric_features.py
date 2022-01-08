'''
Contains classes and methods for calculating various geometric features.
'''

from abc import ABC, abstractmethod
import numpy as np

class Feature(ABC):
    '''
    A base class that highlights all the important methods for feature calculation.
    '''
    def __init__(self, mask):
        self.mask = mask
        self.bin_mask = np.where(mask>200, 1, 0)
    @abstractmethod
    def _calculate_feature(self):
        pass
    def __call__(self):
        return self._calculate_feature()

class Area(Feature):
    '''
    Calculates the Area of the mask by counting cells with value greater than 1.
    '''
    def _calculate_feature(self):
        mask_ = self.bin_mask
        return len(mask_[mask_ > 0])

class Perimeter(Feature):
    '''
    Calculates the Perimeter of the mask by counting number of neighbors.
    '''
    def _calculate_feature(self):
        return self._find_perimeter()
    def _find_perimeter(self):
        perimeter = 0

        for i in range(len(self.bin_mask)):
            for j in range(len(self.bin_mask[0])):
                if self.bin_mask[i][j]:
                    perimeter += (4 - self._count_neighbors(i,j))

        return perimeter
    def _count_neighbors(self, i, j):
        count = 0

        # UP
        if (i > 0 and self.bin_mask[i - 1][j]):
            count += 1

        # LEFT
        if (j > 0 and self.bin_mask[i][j - 1]):
            count += 1

        # DOWN
        if (i < len(self.bin_mask)-1 and self.bin_mask[i + 1][j]):
            count += 1

        # RIGHT
        if (j < len(self.bin_mask[0])-1 and self.bin_mask[i][j + 1]):
            count += 1

        return count

class AreaPerimeter(Feature):
    '''
    Calculates the Area to Perimeter ratio by division.
    '''
    def _calculate_feature(self):
        ar_ = Area(self.mask)
        pe_ = Perimeter(self.mask)
        return ar_()/pe_()
