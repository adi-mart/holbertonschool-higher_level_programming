#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    sorted_names = sorted(name for name in name if "__" not in name)
    for name in sorted_names:
        print(name)
