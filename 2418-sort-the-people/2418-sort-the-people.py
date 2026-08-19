from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = zip(heights, names)
        sorted_paired = sorted(paired, reverse=True)
        
        return [name for height, name in sorted_paired]
