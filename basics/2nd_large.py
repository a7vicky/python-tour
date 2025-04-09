"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
"""

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        sarr = sorted(list(set(arr)))
        if len(sarr) == 1:
            return -1
        else:    
            return sarr[-2]
        
if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    sol = Solution()
    print("Second largest element is:", sol.getSecondLargest(arr))