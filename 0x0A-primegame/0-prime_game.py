#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generates a boolean array for prime numbers up to max_n."""
    sieve = [True] * (max_n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    return sieve

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    
    Args:
        x (int): the number of rounds.
        nums (list of int): array of n values for each round.
        
    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
        If the winner cannot be determined, return None.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    
    # Generate prime sieve for numbers up to max_n
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes <= n for each number up to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # The number of primes in the range 1 to n will determine the winner
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

