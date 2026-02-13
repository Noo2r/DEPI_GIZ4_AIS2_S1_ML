def two_sum(nums, target):
    """
    Finds two numbers in the list that add up to the target.
    Args: nums (list of integers), target (integer)
    returns: indices (list of integers)
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

if __name__ == "__main__":
    print("Enter a list of numbers (comma separated):")
    nums_input = input()
    nums = list(map(int, nums_input.split(",")))
    print("Enter the target number:")
    target_input = int(input())
    result = two_sum(nums, target_input)
    print(result) 