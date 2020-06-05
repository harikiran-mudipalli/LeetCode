class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x:x[0]-x[1])
        sum = 0
        for i in range(int(len(costs)/2)):
            sum += costs[i][0]
        for i in range(int(len(costs)/2), len(costs)):
            sum += costs[i][1]
        return sum
