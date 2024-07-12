# Takes in a number list, returns that list plus 1

def plusOne(self, digits):
        
        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
        return [1] + digits
