from flask import Flask, session, render_template, request
import os
from app.utils import get_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static/pictures')


from app import main, auth, panel
app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(panel.bp)

