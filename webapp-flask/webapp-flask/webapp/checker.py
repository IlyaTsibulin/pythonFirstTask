from flask import session

from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **rwargs):
        if 'logged_in' in session:
            return func(*args, **rwargs)
        return 'You are not logged in.'
    return wrapper