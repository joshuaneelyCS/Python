def lengthOfLastWord(self, s):
        
        s = s.rstrip()
        i = len(s) - 1

        while i >= 0:
            if s[i] == ' ':
                return len(s) - i - 1
            i -= 1
        
        return len(s)

def lengthOfLastWordSimplified(self, s):

        words = s.strip().split()

        if not words:
                return 0

        return len(words[-1])
