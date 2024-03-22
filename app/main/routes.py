from flask import render_template, g
from app.models import Collection
from app.db import session


def index():
    collections = session.query(Collection).limit(5).all()
    return render_template('index.html', user=g.user, collections=collections)
