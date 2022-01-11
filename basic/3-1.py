# this place need to be taken definition of the problem.

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        dic, res, start, = {}, 0, 0



        for i, ch in enumerate(s):
            # when char already in dictionary


            if ch in dic:
                # check length from start of string to index


                # update start of string index to the next index
                res = max(res, i-start)
                start = max(start, dic[ch]+1)


            # add/update char to/of dictionary
            dic[ch] = i



        # answer is either in the beginning/middle OR some mid to the end of string
        return max(res, len(s)-start)


# this is another solution with commenting the codes, however, I doubt that it is valuable for me to see it.
# Because it has all explanation step by step, so, I have to find the value in terms of my phase.
