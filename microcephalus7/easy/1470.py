class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list_x = nums[:n]
        list_y = nums[n:]
        return_list = []
        for i in range(0, n):
            return_list.append(list_x[i])
            return_list.append(list_y[i])
        return return_list