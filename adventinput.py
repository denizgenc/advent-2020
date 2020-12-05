import os
import ssl
import sys
import urllib.request


def get_data(advent_day: int) -> str:
    cookie = get_cookie()
    header = {
            "Cookie": f"session={cookie}",
            }

    request = urllib.request.Request(
        f"https://adventofcode.com/2020/day/{advent_day}/input", headers=header
    )

    with urllib.request.urlopen(request, context=ssl.create_default_context()) as data:
        lines = [str(line, encoding="utf-8").strip() for line in data]
    return lines

def get_cookie():
    try:
        return os.environ["ADVENT_COOKIE"]
    except KeyError:
        print("ADVENT_COOKIE environment variable not set", sys.stderr)
        exit(1)

