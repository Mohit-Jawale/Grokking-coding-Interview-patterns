class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#### Look how elegant the solution is simple use of hash map, there are some previous solutions I have submitted and this one uses the simple idea of same concept of using
##### hashmap but on the second index not on first index.
#### basically if u dont find the first index jst add it u will find it later on.

        index_dict = {}
        for index,num in enumerate(nums):
            if (target-num) in index_dict:
                return([index_dict[target-num],index])
            else:
                index_dict[num]=index
        
