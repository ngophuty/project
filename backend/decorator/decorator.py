from functools import wraps

def user_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kawgrs):
            user_role = 'admin'
            if user_role == 'admin' or user_role == permission:
                return func(*args, **kawgrs)
            else:
                raise Exception("you not permission")
        return wrapper
    return decorator
