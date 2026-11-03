from flask import Flask, g
import os
from app.utils import get_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
if not app.config['SECRET_KEY']:
    raise RuntimeError('Set the SECRET_KEY environment variable, e.g. to the output of: python -c "import secrets; print(secrets.token_hex(32))"')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static/pictures')


@app.before_request
@get_user
def before_request(user):
    g.user = user


from app import main, auth, panel
app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(panel.bp)


from app.commands import fill
app.cli.add_command(fill)
