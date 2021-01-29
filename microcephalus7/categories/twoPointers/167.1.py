def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # Two pointers
    first_idx, last_idx = 0, len(numbers)-1
    while(first_idx < last_idx):
        if numbers[first_idx] + numbers[last_idx] > target:
            last_idx -= 1
        elif numbers[first_idx] + numbers[last_idx] < target:
            first_idx += 1
        else:
            return [first_idx + 1, last_idx + 1]
