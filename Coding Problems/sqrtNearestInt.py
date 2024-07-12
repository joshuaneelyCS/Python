"""Given a non-negative integer x, return the square root of x rounded down
     to the nearest integer. The returned integer should be non-negative as well."""
    
    def mySqrt(self, x):
        left = 1
        right = x

        while True:
            guess = (float(left) + float(right)) / 2
            sqrd = guess * guess

            if int(sqrd) == x:
                return int(guess)
            elif sqrd < x:
                left = guess
            else:
                right = guess
        
        return 0
