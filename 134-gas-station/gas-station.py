class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # If tank goes negative, station 'start_index' through 'i' cannot be the starting point
            if total_tank < 0:
                start_index = i + 1
                total_tank = 0
                
        return start_index