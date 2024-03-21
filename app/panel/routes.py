from flask import render_template, request, redirect, url_for, flash
from flask_httpauth import HTTPBasicAuth
from slugify import slugify
from app import app
import os
from app.models import Picture, Collection
from app.db import session

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == '12345':
        return username


@auth.login_required
def index():
    return render_template('panel/index.html')


@auth.login_required
def create_picture():
    if request.method == 'GET':
        return render_template('panel/upload.html')

    file = request.files.get('picture')
    filetype = file.content_type.split('/')[1]
    filename = f"{slugify(request.form.get('name'), separator="_")}.{filetype}"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    picture = Picture(name=filename)
    session.add(picture)
    session.commit()

    flash('Picture uploaded at')
    return redirect(url_for('panel.index'))


@auth.login_required
def create_collection():
    if request.method == 'GET':
        return render_template('panel/collection.html')

    data = request.form.keys()
    i = iter(data)

    c_name = request.form.get('collection_name')
    collection = Collection(name=c_name)
    session.add(collection)
    session.commit()

    next(i)

    for ind, key in enumerate(i):
        pic_name = request.form.get(f'{key}')
        pic_desc = request.form.get(f'description_{ind}')

        file = request.files.get(f'picture_{ind+1}')
        filetype = file.content_type.split('/')[1]
        filename = f"{slugify(str(pic_name), separator="_")}.{filetype}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_picture = Picture(name=pic_name, description=pic_desc, uri=filename, collection_id=collection.id)
        session.add(new_picture)
        session.commit()
        next(i)
    return '200'


@auth.login_required
def update_picture():
    return 'edit'


@auth.login_required
def update_collection():
    return 'edit collection'


@auth.login_required
def delete_picture():
    return 'delete picture'


@auth.login_required
def delete_collection():
    return 'delete collection'
