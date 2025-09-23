#!/usr/bin/python3
"""Module defining an abstract base class for animals and
concrete subclasses for Dog and Cat."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses
        to return the sound of the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""
    def sound(self):
        """Return the sound made by the dog."""
        return ("Bark")


class Cat(Animal):
    """Concrete class representing a cat."""
    def sound(self):
        """Return the sound made by the cat."""
        return ("Meow")
