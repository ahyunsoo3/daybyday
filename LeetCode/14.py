def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

x = input().strip()
print(longestCommonPrefix(x))


# reference :
# https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution