from flask import Flask
from bluelog.blueprints.auth import auth_bp
from bluelog.settings import config


app = Flask('__name__')

app.register_blueprint(auth, url_prefix='/auth')
app.config.from_object(config[config_name])


@app.route('hello')
def say_hello():
    return 'Hello!'



