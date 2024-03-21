from app.db import session
from app.models import User
from flask import render_template, request, flash, redirect, url_for
from flask import session as s
from .utils import generate_hash, check_password
from app.utils import get_user


@get_user
def signup(user):
    if user:
        return redirect(url_for('main.index'))

    title = 'Signup'

    if request.method == 'GET':
        return render_template('auth/signup.html', title=title)

    username = request.form.get('username')
    password = request.form.get('password')
    user = session.query(User).filter_by(username=username).first()

    if user:
        flash('Username already in use.')
        return render_template('auth/signup.html', title=title)

    user = User(username=username, password=generate_hash(password))
    session.add(user)
    session.commit()
    s['user'] = user.id

    return redirect(url_for('main.index'))


@get_user
def login(user):
    if user:
        return redirect(url_for('main.index'))

    title = 'Login'

    if request.method == 'GET':
        return render_template('auth/signup.html', title=title)

    username = request.form.get('username')
    password = request.form.get('password')
    user = session.query(User).filter_by(username=username).first()

    if not user:
        flash('User not founded.')
        return render_template('auth/signup.html', title=title)

    if not check_password(password, user.password):
        flash('Wrong password.')
        return render_template('auth/signup.html', title=title)

    s['user'] = user.id
    return redirect(url_for('main.index'))


def logout():
    s['user'] = None
    return redirect(url_for('main.index'))
