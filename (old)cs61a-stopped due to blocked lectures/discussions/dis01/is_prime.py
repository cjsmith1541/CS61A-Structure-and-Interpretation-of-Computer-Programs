def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False
    y = 2
    while y < n:
        if n % y == 0:
            return False
        y += 1
    return True
