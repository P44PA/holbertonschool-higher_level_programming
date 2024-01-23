#!/usr/bin/python3

class LockedClass:
    """A class that prevents the dynamic creation of new instance attributes,
    except for the attribute 'first_name'.

    Attributes:
    __slots__ (tuple): A tuple specifying the allowed attribute names.

    Methods:
    __setattr__(self, name, value): Overrides the default attribute setting
        behavior to allow only the attribute 'first_name' to be set."""
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)

# Example usage:
locked_instance = LockedClass()
locked_instance.first_name = 'John'  # Allowed
# locked_instance.last_name = 'Doe'  # Raises AttributeError

