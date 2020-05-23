from typing import List

def solution(arr: List) -> int:
    """
    This should run in O(N) time since we iterate through the list once and track sums as we go.
    Worst case, this would require O(N) additional space since we use a map to track calculated sums
    of digits and could have a different sum for every member of the original list.
    """
    def _sum_of_digits(integer):
        int_as_str = str(integer)
        digits_as_ints = [int(digit) for digit in int_as_str]
        return sum(digits_as_ints)

    sums_so_far = dict()
    max_sum_so_far = -1
    for num in arr:
        sum_of_digits = _sum_of_digits(num)
        if sum_of_digits in sums_so_far:
            new_sum = sums_so_far[sum_of_digits] + num
            if new_sum > max_sum_so_far:
                max_sum_so_far = new_sum
            sums_so_far[sum_of_digits] = max(sums_so_far[sum_of_digits], num)
        else:
            sums_so_far[sum_of_digits] = num

    return max_sum_so_far
