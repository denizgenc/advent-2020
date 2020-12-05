from typing import List

import adventinput


def password_validator(password_list: List[str]) -> int:
    num_valid = 0
    for line in password_list:
        counts, letter, password = line.split(" ")
        min_count, max_count = [int(s) for s in counts.split("-")]
        letter = letter[0]
        if password.count(letter) in range(min_count, max_count + 1):
            num_valid += 1

    return num_valid


passwords = adventinput.get_data(2)

day2_part1_answer = password_validator(passwords)
print(f"Number of valid passwords = {day2_part1_answer}")
