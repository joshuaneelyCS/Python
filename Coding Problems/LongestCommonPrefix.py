# Given a list of strings, find the longest shared prefix. If none, return ""

def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        def longestCommonPrefixRec(strs, left, right):
            if left == right:
                return strs[left]
            else:
                mid = (left + right) / 2
                l = longestCommonPrefixRec(strs, left, mid)
                r = longestCommonPrefixRec(strs, mid+1, right)
                return commonPrefix(l,r)

            return

        def commonPrefix(left, right):
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        return longestCommonPrefixRec(strs, 0, len(strs)-1)
