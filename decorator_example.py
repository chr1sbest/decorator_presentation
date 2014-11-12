from functools import wraps
from time import time as now

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Prints the execution time of a function."""
        # Time the execution of the function.
        start_time = now()
        result = func(*args, **kwargs) # Decorated function executes here.
        end_time = now()

        # Calculate and print the execution time.
        exec_time = end_time - start_time
        print "Execution time was {0} ms".format(exec_time)
        return result
    return wrapper
