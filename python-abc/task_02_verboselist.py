#!/usr/bin/python3
class VerboseList(list):
    """A subclass of list that prints messages on item addition and removal."""

    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable
        and print a message."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove an item from the list and print a message."""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Remove and return an item at the given index and print a message."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")


if __name__ == "__main__":
    VL = VerboseList([2, 3, 4, 5])
    VL.append(6)
    VL.extend([7, 8, 9])
    VL.remove(8)
    VL.pop()
