
# - 1 -
# sample = [1,2,3,4,5]
# tlist = list(map(lambda x: x + 10, sample))
#
# print(tlist)

# -------------------------------------------------------

# - 2 -
# tlist = [n + 1 for n in range(1, 10 + 1) if n % 2 == 1]
#
# print(tlist)

# -------------------------------------------------------

# - Generator -

# def get_natural_number():
#     yield 1
#     yield 'string'
#     yield True
#
# g = get_natural_number()
# for _ in range(0, 3):
#     print(next(g))

# -------------------------------------------------------

# - list range -
# print(list(range(5)))
#
#
# for i in range(5):
#     print(i, end='  ')

# -------------------------------------------------------

# - enumerate -
# a = [1,2,3,4,5,123,42,5]

# for i in range(len(a)):
#     print(i, a[i])
#
# for i, v in enumerate(a):
#     print(i, v)
#

# -------------------------------------------------------

# - type -
# print (type(5 / 3))

# - divmod -
# print ( divmod(5, 3), end=' ')
#
# print ('A', 'B', sep=',')
#
# # for debugging
#
# a = ['a', 'b']
# print(a)
# print(' '.join(a))

# -------------------------------------------------------
#
# class MyClass(object):
#     def testOne(self):
#         pass

#
# for n in range(1, 15 + 1):
#     print(n, n ** 2, 2 ** n)
#
#
# # object > int > bool
#
# a = set()
# print (type(a))
#
# a = [1, 'Hello', True
#     ]
# print(a)

# - P -

def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

checkPalindrome = isPalindrome()
print (checkPalindrome('asdfeseee') )