from flask import render_template
from app.utils import get_user
from app.models import Collection
from app.db import session


@get_user
def index(user):
    collections = session.query(Collection).limit(5).all()
    return render_template('index.html', user=user, collections=collections)
