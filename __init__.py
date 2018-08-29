from flask import Flask, Blueprint, render_template

app = Flask(__name__)


from iismonitorpy.main.routes import home_api

app.register_blueprint(home_api, url_prefix='/')