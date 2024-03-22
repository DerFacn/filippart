from app.db import session
from app.models import User
from flask import render_template, request, flash, redirect, url_for, g
from flask import session as s
from .utils import generate_hash, check_password


def signup():
    if g.user:
        return redirect(url_for('main.index'))  # If already logged in - redirect

    title = 'Signup'

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = session.query(User).filter_by(username=username).first()

        if user:
            flash('Username already in use.')
            return render_template('auth/signup.html', title=title)

        user = User(username=username, password=generate_hash(password))
        session.add(user)
        session.commit()
        s['user_id'] = user.id

        return redirect(url_for('main.index'))

    return render_template('auth/signup.html', title=title)  # Opened in browser


def login():
    if g.user:
        return redirect(url_for('main.index'))

    title = 'Login'

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = session.query(User).filter_by(username=username).first()

        if not user:
            flash('User not founded.')
            return render_template('auth/signup.html', title=title)

        if not check_password(password, user.password):
            flash('Wrong password.')
            return render_template('auth/signup.html', title=title)

        s['user_id'] = user.id
        return redirect(url_for('main.index'))

    return render_template('auth/signup.html', title=title)


def logout():
    s['user_id'] = None
    g.user = None
    return redirect(url_for('main.index'))
