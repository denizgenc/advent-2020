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


def official_policy(password: str, letter: str, index1: int, index2: int) -> bool:
    return (password[index1 - 1] == letter) ^ (password[index2 - 1] == letter)


passwords = adventinput.get_data(2)

day2_part1_answer = password_validator(passwords, old_policy)
print(f"Number of valid passwords = {day2_part1_answer}")
day2_part2_answer = password_validator(passwords, official_policy)
print(f"Number of actually valid passwords = {day2_part2_answer}")
