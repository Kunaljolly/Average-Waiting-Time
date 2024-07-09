class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        ft = customers[0][1] + customers[0][0]
        count = customers[0][1]
        for x in range(n-1):
            if ft <= customers[x+1][0]:
                count += customers[x+1][1] 
                ft = customers[x+1][1] + customers[x+1][0]
            else:
                count +=  (((ft) - customers[x+1][0]) + customers[x+1][1])
                ft += customers[x+1][1]
        return count/n

