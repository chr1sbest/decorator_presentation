from time import time as now

def some_calculation(value):
    """Add one to a value."""
    # Time the execution of the function.
    start_time = now()
    value = value + 1
    end_time = now()

    # Calculate and print the execution time.
    exec_time = end_time - start_time
    print "Execution time was {0}ms".format(exec_time)

    # Finally, return the result of the increment.
    return value





































































































def some_other_calculation(value, factor):
    """Multiply a value by a factor."""
    start_time = now()
    value = value * factor
    end_time = now()
    exec_time = end_time - start_time
    print "Execution time was {0}ms".format(exec_time)
    return value

def the_final_calculation(value, increment_by_one=False):
    """Double the value and optionally increment by 1."""
    start_time = now()
    value =  (value * 2) + 1 if increment_by_one else value * 2
    end_time = now()
    exec_time = end_time - start_time
    print "Execution time was {0}ms".format(exec_time)
    return value
