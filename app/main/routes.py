from flask import render_template
from app.utils import get_user
from app.models import Picture
from app.db import session


@get_user
def index(user):
    return render_template('index.html', user=user)


def pictures():
    pictures_ = session.query(Picture).all()
    return render_template('main/pictures.html', pictures=pictures_)
