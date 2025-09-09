#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for letter in reversed(roman_string):
        value = dict.get(letter, 0)
        if value < prev:
            result -= value
        else:
            result += value
        prev = value
    return (result)
