from flask import render_template
from app.models import Collection
from app.db import session


def index():
    collections = session.query(Collection).limit(5).all()
    return render_template('index.html', collections=collections)
