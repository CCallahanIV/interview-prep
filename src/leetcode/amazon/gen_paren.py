"""
Taken from: https://leetcode.com/problems/generate-parentheses/
"""

def gen_paren_solution(n):
    out = []
    if n == 0:
        return out
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            # We've built a complete solution, add to output.
            out.append(s)
            return
        if left < n:
            # number of left brackets is less than `n`, add another.
            backtrack(s + '(', left + 1, right)
        if right < left:
            # don't have enough right brackets, add one.
            backtrack(s + ')', left, right + 1)

    backtrack()
    return out
