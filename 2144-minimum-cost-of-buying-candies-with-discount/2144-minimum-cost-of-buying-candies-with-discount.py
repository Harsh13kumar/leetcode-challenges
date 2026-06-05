class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse =True)
        minCost=0
        for i in range(0,len(cost),3):
            group = cost[i:i+3]
            if len(group)==3:
                minCost = minCost+group[0] + group[1]
            else:
                minCost=minCost+sum(group)
        return minCost 
