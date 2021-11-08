# dfs with memo. For current week, we could stay at current city, or fly to other citys if we could fly, then get the max vacation day from the results for next week

def maxVacationDays(self, flights, days):
        N = len(flights)
        K = len(days[0])
        memo = {}
        
        # start from city 0 and week 0
        return self.dfs(0, 0, flights, days, N, K, memo)
            
    def dfs(self, city, week, flights, days, N, K, memo):
        if (city, week) in memo:
            return memo[(city, week)]
        
        if week == K:
            return 0
        
        maxDay = 0 
        for i in range(N):
            # we could either stay in current city or fly to other city at current week
            if i == city or flights[city][i] == 1:
                # update maxDay using the result for next week
                maxDay = max(maxDay, days[i][week] + self.dfs(i, week + 1, flights, days, N, K, memo))
        
        memo[(city, week)] = maxDay
        return maxDay