def two_sum_solution_brute_force(nums, target):
    """O(n)^2"""
    unique_pairs = set()
    nums = sorted(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                unique_pairs.add((nums[i], nums[j]))
    
    return len(unique_pairs)

    
def two_sum_solution(nums, target):
    """O(n)"""
    unique_pairs, comp = set(), set()
    for num in nums:
        c = target - num
        if c in comp:
            # Sort the order
            unique_pairs.add((num, c) if num < c else (c, num))
        comp.add(num)
    print(unique_pairs)
    return len(unique_pairs)
