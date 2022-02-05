
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





