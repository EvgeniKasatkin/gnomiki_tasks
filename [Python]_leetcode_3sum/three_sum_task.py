
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums[:] = sorted(nums)

        for index_, value_1 in enumerate(nums):
            if index_ and value_1 == nums[index_ - 1]:
                continue

            index_value_2 = index_ + 1
            index_value_3 = len(nums) - 1
            while index_value_2 < index_value_3:
                three_sum = value_1 + nums[index_value_2] + nums[index_value_3]
                if three_sum < 0:
                    index_value_2 += 1
                elif three_sum > 0:
                    index_value_3 -= 1
                else:
                    result.append([value_1, nums[index_value_2], nums[index_value_3]])
                    index_value_2 += 1
                    while nums[index_value_2] == nums[index_value_2 - 1] and index_value_2 < index_value_3:
                        index_value_2 += 1

        return result


if __name__ == '__main__':
    nums = [0,2,3,4,1,-3,4,-3,-2, -1,-1]
    test = Solution().threeSum(nums = nums)

"""
    Input: brakets_string = [0,2,3,4,1,-3,4,-3,-2, -1,-1]
    Output: [[-3, -1, 4],
             [-3, 0, 3],
             [-3, 1, 2],
             [-2, -1, 3],
             [-2, 0, 2],
             [-1, -1, 2],
             [-1, 0, 1]]
"""






