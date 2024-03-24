import click
import string
import random
from app.models import Picture, Collection, User
from app.db import session
from flask.cli import with_appcontext
from app.auth.utils import generate_hash


def randomizer(count: int) -> str:
    words = ""
    for i in range(count):
        letters = random.randint(4, 12)
        word = random.choice(string.ascii_uppercase)
        for m in range(letters):
            word += random.choice(string.ascii_lowercase)
        words = words + f'{word} '
    return words


@click.group(help='Base filling commands')
def fill():
    pass


@fill.command('gallery', help='Fill the table with fake pictures')
@with_appcontext
def gallery():
    for c in range(5):
        new_collection = Collection(name=f'Collection {c}', preview='image.png', description=f'{randomizer(1)}')
        session.add(new_collection)
        session.commit()

        for p in range(5):
            name = randomizer(1)
            description = randomizer(30)
            new_picture = Picture(
                name=f'Picture {name}',
                description=description,
                uri='image.png',
                price='50',
                collection_id=new_collection.id
            )
            session.add(new_picture)
            session.commit()
    click.echo('Fake gallery successfully loaded!')


@fill.command('admin', help='Create an admin account')
@click.password_option()
@with_appcontext
def admin(password):
    new_admin = User(username='admin', password=generate_hash(password))
    session.add(new_admin)
    session.commit()
    click.echo('Admin successfully created!')
