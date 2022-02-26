from os import set_inheritable
from typing import List
from fpypeline.shape import Shape


class Polygon(Shape):
    
    def __init__(self, side_lengths: List[float]=None):
        self.side_lengths = side_lengths
        
    def compute_perimeter(self) -> float:
        return sum(self.side_lengths)
    
    def get_number_of_edges(self) -> int:
        return len(self.side_lengths)
    
