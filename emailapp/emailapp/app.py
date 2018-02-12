from flask import Flask
from emailapp.views.index import bp as index_bp 
from emailapp.views.createemail import bp as createemail_bp
app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(createemail_bp)