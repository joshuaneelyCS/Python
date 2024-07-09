def isValid(self, s):
    stack = []
    pMap = { '(':')', '{': '}','[': ']'}

    for i in s:
        if i in pMap:
            stack.append(i)
        else:
            if not stack or pMap[stack.pop()] != i:
                return False

    return not stack
