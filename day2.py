from typing import Callable, List

import adventinput


def password_validator(
    password_list: List[str], policy: Callable[[str, str, int, int], bool]
) -> int:
    num_valid = 0
    for line in password_list:
        counts, letter, password = line.split(" ")
        num1, num2 = [int(s) for s in counts.split("-")]
        letter = letter[0]
        if policy(password, letter, num1, num2):
            num_valid += 1

    return num_valid


def old_policy(password: str, letter: str, min_count: int, max_count: int) -> bool:
    return password.count(letter) in range(min_count, max_count + 1)


passwords = adventinput.get_data(2)

day2_part1_answer = password_validator(passwords, old_policy)
print(f"Number of valid passwords = {day2_part1_answer}")
