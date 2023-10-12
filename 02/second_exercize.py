"""Module with the decorator required by the task"""

import time
from collections import deque


def mean(k):
    """Decorator for calculate least recent calls duration time"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, 'least_recent_calls'):
                wrapper.least_recent_calls = deque(maxlen=k)
            start_time = time.time()
            result = func(*args, **kwargs)
            wrapper.least_recent_calls.append(time.time() - start_time)
            average_time = sum(wrapper.least_recent_calls) / len(wrapper.least_recent_calls)
            return result, average_time
        return wrapper
    return decorator
