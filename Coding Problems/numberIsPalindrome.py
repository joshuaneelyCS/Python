# Checks if a number is a palindrome, negatives return false

def numberIsPalindrome(self, x):
        if x < 0:
            return False
        
        if x != 0 and x % 10 == 0:
            return False

        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        
        return x == reversed_number or x == reversed_number // 10
