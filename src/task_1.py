from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Create and return a fibonacci function with caching.

    :return: A function fibonacci(n) that computes the nth Fibonacci number using cache.
    """
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
