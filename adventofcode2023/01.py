from typing import List, Dict

digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

numbers.update(digits)



def numberfinder(input_string: str, valid_values: Dict):
    _, found = min(
        filter(lambda x: x[0] >= 0,
               tuple(
                    (input_string.find(search), search)
                    for search in valid_values.keys()
               )
        )
    )

    _, found_last = max(
        (input_string.rfind(search), search)
        for search in valid_values.keys()
    )

    return int(f"{valid_values[found]}{valid_values[found_last]}")


def process_numberfinder_string(input_string: str):
    """
    one112one

    11121 => 11
    """
    for word, number in numbers.items():
        input_string.replace(word, str(number))

    return input_string


def sum_numberfinders(number_strings: List[str]):
    return sum(
        numberfinder(s, digits) for s in number_strings
    )


def sum_preprocessed_numberfinders(number_strings: List[str]):
    return sum(
        numberfinder(s, numbers)
        for s in number_strings
    )


def test_numberfinder():
    assert numberfinder("1abc2", digits) == 12
    assert numberfinder("pqr3stu8vwx", digits) == 38
    assert numberfinder("a1b2c3d4e5f", digits) == 15
    assert numberfinder("treb7uchet", digits) == 77


def test_sum_numberfinder():
    assert sum_numberfinders("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split()) == 142


def test_preprocessed_numberfinder():
    assert sum_preprocessed_numberfinders("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split()) == 281


if __name__ == '__main__':
    print(sum_numberfinders(open("input/01").read().splitlines()))
    print(sum_preprocessed_numberfinders(open("input/01").read().splitlines()))

