# Description: Time Complexity of a Function using Decorator in Python to measure execution time for any function

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.6f}s")
        return result
    return wrapper