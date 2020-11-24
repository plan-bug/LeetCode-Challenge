class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])  # example num2 = [1,3,4,2]
        # stack = [1]

        for i in range(1, len(nums2)):
            # num2[1] = 3, stack[-1] = 1 / num2[2] = 4, stack[-1] = 3 / num2[3] =2, stack[-1] = 4
            while stack and nums2[i] > stack[-1]:
                # mapping = { 1: 3} / mapping = {1:3, 3: 4}
                mapping[stack[-1]] = nums2[i]
                stack.pop()  # stack = [] / stack = [] / stack = [4]
            # stack = [3] / stack = [4] / stack = [4, 2]
            stack.append(nums2[i])
        for element in stack:
            mapping[element] = -1  # mapping = {1:3, 3:4, 4: -1, 2: -1}

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])  # result = [-1, 3, -1]
        return result
