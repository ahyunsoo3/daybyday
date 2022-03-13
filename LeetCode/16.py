class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):



            j, k = i + 1, len(num) - 1 # k is the end of the array, j is just near the i.

            while j < k: # such that index of j is not approved from this condition.
                sum = num[i] + num[j] + num[k] # consecutive?



                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target): # why the result standard is needed? -> you need to operate your simulation in your brain. Test case can say the answer.
                    result = sum
                    # The smaller the difference between two numbers, the closer the answer is.
                    # If so, there should also be a code that gives the correct answer when the difference is minimal.

                if sum < target: # only j move because of requiring slight variance.
                    j += 1
                elif sum > target:
                    k -= 1





        return result






# reference :
# https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution