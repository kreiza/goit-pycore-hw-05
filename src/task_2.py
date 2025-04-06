import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Yield all real numbers from the given text.

    :param text: The input text containing real numbers separated by spaces.
    :yield: Each real number as a float.
    """
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Sum all real numbers in the text using the provided generator function.

    :param text: The input text containing real numbers.
    :param func: A function that returns a generator yielding real numbers from text.
    :return: The total sum of the numbers.
    """
    return sum(func(text))
