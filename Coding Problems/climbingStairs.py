"""You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways
     can you climb to the top?"""

    def climbStairs(self, n):
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        table = [0] * (n+1)
        table[1] = 1
        table[2] = 2

        for i in range(3, n + 1):
            table[i] = table[i-1] + table[i-2]
        
        return table[n]
