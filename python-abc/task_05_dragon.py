#!/usr/bin/python3

class SwimMixin:
    """Mixin class to add swimming capability."""
    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying capability."""
    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon, inheriting swimming and
    flying capabilities."""
    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")

    def habitat(self):
        """Describe the habitat of the dragon."""
        print("The dragon lives in caves")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.roar()
    dragon.swim()
    dragon.fly()
    dragon.habitat()
