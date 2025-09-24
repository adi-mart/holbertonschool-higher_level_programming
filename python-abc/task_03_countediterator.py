#!/usr/bin/python3
"""Module defining a CountedIterator class that wraps an iterator
and counts the number of items iterated over."""


class CountedIterator:
    """Class that wraps an iterator and counts the number of
    items iterated over."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.__iterator = iter(iterable)
        self.__count = 0

    def __iter__(self):
        """Return the __iterator object itself."""
        return (self)

    def __next__(self):
        """Return the next item from the __iterator and
        increment the __count."""
        item = next(self.__iterator)
        self.__count += 1
        return (item)

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return (self.__count)


if __name__ == "__main__":
    data = [10, 20, 30]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()}"
                  f"items iterated.")
    except StopIteration:
        print("No more items.")
