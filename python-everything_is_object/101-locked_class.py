#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} object has no attribute '{name}'")
        else:
            object.__setattr__(self, name, value)

# Example usage:
locked_instance = LockedClass()

# Allowed attribute assignment
locked_instance.first_name = 'John'

# Attempting to assign a new attribute other than 'first_name' will raise an error
try:
    locked_instance.last_name = 'Doe'
except AttributeError as e:
    print(e)  # Output: LockedClass object has no attribute 'last_name'

