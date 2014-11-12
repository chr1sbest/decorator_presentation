from decorator_example import timer

@timer
def some_calculation(value):
    """Add one to a value."""
    return value + 1

@timer
def some_other_calculation(value, factor):
    """Multiply a value by a factor."""
    return value * factor

@timer
def the_final_calculation(value, increment_by_one=False):
    """Double a value and optionally increment by 1."""
    return (value * 2) + 1 if increment_by_one else value * 2
