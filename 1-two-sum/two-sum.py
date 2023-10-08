class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        num_index = 0
        for num in nums:
            second_num_index = 0
            for second_num in nums:
                if num + second_num == target:
                    if num_index != second_num_index:
                        return(num_index, second_num_index)
                second_num_index += 1
            num_index += 1
