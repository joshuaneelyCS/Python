# input two strings of binary numbers

def addBinary(self, a, b):
        ra = len(a)-1
        rb = len(b)-1

        carry = 0
        result = []

        while ra >= 0 or rb >= 0 or carry:
            
            num = carry
            if ra >= 0:
                num += int(a[ra])
                ra -= 1
            if rb >= 0:
                num += int(b[rb])
                rb -= 1
            
            carry = num // 2
            result.append(str(num % 2))

        return ''.join(reversed(result))
