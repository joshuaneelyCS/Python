# Given a list of strings, find the longest shared prefix. If none, return ""

def longestCommonPrefix(self, strs):
        while True:
            result = ""
            if len(strs) == 1:
                return strs[0]
            for i in range (0,len(strs[0])):
                letter = strs[0][i]
                for word in strs:
                    if i == len(word):
                        return result
                    if word[i] != letter:
                        return result
                result += letter
            return result
