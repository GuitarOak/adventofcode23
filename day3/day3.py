import re
from typing import Generator, Tuple, List

# Open the file and read the lines into a list
lines: List[str] = open("day3/input.txt").read().splitlines()


def is_symbol(char: str) -> bool:
    """
    Checks if a character is a symbol.

    Parameters:
    char (str): The character to check.

    Returns:
    bool: True if the character is a symbol, False otherwise.
    """
    return char != "." and not char.isdigit()


def get_numbers() -> Generator[Tuple[int, str, int, int, int], None, None]:
    for i, line in enumerate(lines):
        # Loop over each number in the line
        for match in re.finditer(r"\d+", line):
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            yield i, line, start_index, end_index, number


count = 0

# Iterate over the generated tuples
for (
    i,
    line,
    start_index,
    end_index,
    number,
) in get_numbers():
    if (start_index >= 0 and is_symbol(line[start_index])) or (
        end_index < len(line) and is_symbol(line[end_index])
    ):
        count += number
        continue

    for j in range(start_index, end_index + 1):
        if j >= len(line):
            continue

        if (i > 0 and is_symbol(lines[i - 1][j])) or (
            i < len(lines) - 2 and is_symbol(lines[i + 1][j])
        ):
            count += number
            break

print(count)