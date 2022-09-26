class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        for indx,citation in enumerate(citations):
            if indx>=citation:
                return indx
        return len(citations)