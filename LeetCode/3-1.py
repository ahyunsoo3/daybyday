# this place need to be taken definition of the problem.

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        dic, res, start, = {}, 0, 0



        for i, ch in enumerate(s): # ch is nowhere defined, so, it is a teomporal role.


            if ch in dic: # find difference from elemnets between ch and dic.


                res = max(res, i-start) # max menas that it is larger than other.
                start = max(start, dic[ch]+1)



            dic[ch] = i



        return max(res, len(s)-start)






# - i -
# this is another solution with commenting the codes, however, I doubt that it is valuable for me to see it.
# Because it has all explanation step by step, so, I have to find the value in terms of my phase.
