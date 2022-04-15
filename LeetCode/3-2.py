class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):


            if value in dicts: # this process is unnormal for me to understand procesdure, so it makes me question
                # the value have that I attempt to understand this
                # when do people select their tasks in their way?
                # The answer is what do you want to focus on, so people should know what they want result from this
                # I thought, I wanted to all everything, but it makes me confused by selecting procedure.
                # I thought that the attitude gives me a lot of things, however, narrowing down it is more important than
                # that attitude. I understand what I aim for, but, it is needed for arranging.
                # If you don't, you wouldn't get anything, which provides you with deeper concept that is needed for obtainng the advanced perspectives.




                sums = dicts[value] + 1


                if sums > start:
                    start = sums



            num = i - start + 1



            if num > maxlength:
                maxlength = num


            dicts[value] = i


        return maxlength









