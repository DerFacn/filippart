from flask import render_template, request, redirect, url_for, flash
from slugify import slugify
from app import app
import os
from app.models import Picture, Collection
from app.db import session
from app.utils import admin_required


@admin_required
def index():
    collections = session.query(Collection).all()
    return render_template('panel/index.html', collections=collections)


@admin_required
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


@admin_required
def create_collection():
    if request.method == 'GET':
        return render_template('panel/collection.html')
    #  Creating new collection
    c_name = request.form.get('collection_name')
    c_desc = request.form.get('collection_description')

    preview = request.files.get('collection_preview')
    filetype = preview.content_type.split('/')[1]
    filename = f"{slugify(str(preview.filename), separator="_")}.{filetype}"
    preview.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    collection = Collection(name=c_name, description=c_desc, preview=filename)
    session.add(collection)
    session.commit()
    #  Creating new pictures
    group_length = 3
    data = request.form

    for i in range(1, len(data) // group_length + 1):
        group_keys = [f'name_{i}', f'description_{i}', f'price_{i}']
        group_values = [data[key] for key in group_keys]

        file = request.files.get(f'picture_{i}')
        filetype = file.content_type.split('/')[1]
        filename = f"{slugify(str(group_values[0]), separator="_")}.{filetype}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_picture = Picture(
            name=group_values[0],
            description=group_values[1],
            uri=filename,
            price=group_values[2],
            collection_id=collection.id
        )

        session.add(new_picture)
        session.commit()

    return redirect(url_for('panel.index'))


@admin_required
def update_picture():
    return 'edit'


@admin_required
def update_collection():
    return 'edit collection'


@admin_required
def delete_picture():
    return 'delete picture'


@admin_required
def delete_collection():
    return 'delete collection'
