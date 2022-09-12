class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # not necessary
        if n == 0:
            return len(tasks)
        
        count = Counter(tasks)
        
        # get the highest frequency
        most = count.most_common()[0][1]
        
        # get the number of chars of the highest frequency
        num_of_most = len([i for i, num in count.items() if num == most])
        
        # use mathematic method
        return max((most - 1) * (n + 1) + num_of_most, len(tasks))