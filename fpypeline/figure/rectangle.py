import numpy as np

from fpypeline.polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths)
        assert (
            len(self.side_lengths) == 2
        ), "A rectangle can only have 2 different sides."

        assert (
            self.side_lengths[0] != self.side_lengths[1]
        ), "A rectangle can only have 2 different sides."

    def area(self):
        return np.prod(self.side_lengths)
