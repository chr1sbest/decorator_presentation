from decorator_example import time_decorator

@time_decorator
def some_calculation(value):
    """Add one to a value."""
    return value + 1

@time_decorator
def some_other_calculation(value, factor):
    """Multiply a value by a factor."""
    return value * factor

@time_decorator
def the_final_calculation(value, increment_by_one=False):
    """Double a value and optionally increment by 1."""
    return (value * 2) + 1 if increment_by_one else value * 2
