cache = {}
def isMatch(self, s, p):
    if (s, p) in self.cache:
        return self.cache[(s, p)]
    if not p:
        return not s
    if p[-1] == '*':
        if self.isMatch(s, p[:-2]):
            self.cache[(s, p)] = True
            return True
        if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
            self.cache[(s, p)] = True
            return True
    if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
        self.cache[(s, p)] = True
        return True
    self.cache[(s, p)] = False
    return False





# Reference :
# https://leetcode.com/problems/regular-expression-matching/discuss/5678/Fast-Python-solution-with-backtracking-and-caching-%2B-DP-solution
# There are more answers provided from the creator who makes this. (DP ver)

# In this time, I should be better to not understand this code because it has a trait that I follow some logic that I don't know this time.
# If I spend my time on this, I could understand this quickly, however, in terms of time consuming of learning process, it shouldn't be that.
# Test