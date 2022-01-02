'''
Contains classes and methods for calculating various geometric features.
'''

import numpy as np

class Feature:
    '''
    A base class that highlights all the important classes for feature calculation. 
    '''

    def __init__(self, mask):
        self.mask = mask
    def _calculate_feature(self):
        return None
    def __call__(self):
        return self._calculate_feature()

class Area(Feature):
    '''
    Calculates the Area of the mask by counting cells with value greater than 1.
    '''
    def _calculate_feature(self):
        return len(np.where(self.mask > 0,self.mask))

class Perimeter(Feature):
    '''
    Calculates the Perimeter of the mask by counting number of neighbors.
    '''
    def _calculate_feature(self):
        return self._find_perimeter()
    def _find_perimeter(self):
        perimeter = 0

        for i in range(len(self.mask)):
            for j in range(len(self.mask[0])):
                if self.mask[i][j]:
                    perimeter += (4 - self._count_neighbors(i,j))

        return perimeter
    def _count_neighbors(self, i, j):
        count = 0

        # UP
        if (i > 0 and self.mask[i - 1][j]):
            count += 1

        # LEFT
        if (j > 0 and self.mask[i][j - 1]):
            count += 1

        # DOWN
        if (i < len(self.mask)-1 and self.mask[i + 1][j]):
            count += 1

        # RIGHT
        if (j < len(self.mask[0])-1 and self.mask[i][j + 1]):
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
