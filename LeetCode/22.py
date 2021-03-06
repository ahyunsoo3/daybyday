class slv:
    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))


print(slv().generateParenthesis(1))


# Ref : https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
# Ref : https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

# - Q -
# what is stored at q?
# when a function is closed, what does happen with regard to memory?