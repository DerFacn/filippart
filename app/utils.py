from flask import session as s
from app.models import User
from app.db import session
from functools import wraps


def get_user(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        kwargs['user_'] = None
        user_id = s.get('user_id')
        if user_id:
            user = session.query(User).filter_by(id=user_id).first()
            kwargs['user_'] = user
            return func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped
