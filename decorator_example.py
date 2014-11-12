from functools import wraps
from time import time as now

# If func not decorated,          func() runs as -> func()
# If func decorated with @timer,  func() runs as -> timer(func())

def timer(func):    # Takes decorated function as the sole parameter.
    @wraps(func)    # Passes decorated function's metadata to wrapper.
    def wrapper(*args, **kwargs):
        """Prints the execution time of a function."""
        start_time = now()
        result = func(*args, **kwargs) # Decorated function executes.
        end_time = now()
        exec_time = end_time - start_time
        print "Execution time was {0}ms".format(exec_time)
        return result
    return wrapper
