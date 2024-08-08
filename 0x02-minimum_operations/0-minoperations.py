#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to obtain
exactly `n` H characters in a file using only "Copy All" and "Paste".
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to get exactly `n` H characters.
    
    Parameters:
    n (int): The number of H characters desired.

    Returns:
    int: Minimum number of operations required. Returns 0 if `n` is less than or equal to 1.
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations

