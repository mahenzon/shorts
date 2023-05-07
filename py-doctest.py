"""
Python doctest demo
"""


def compute_average(nums):
    """
    Compute the average of a list of numbers.

    >>> compute_average([1, 2, 3, 4])
    2.5
    >>> compute_average([0, 5, 10])
    5.0
    >>> compute_average([-2, 2, -5, 5])
    0.0

    If the input is an empty list,
    return None.

    >>> compute_average([])
    """
    if not nums:
        return None
    return sum(nums) / len(nums)
