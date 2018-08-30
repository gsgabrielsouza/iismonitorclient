from flask import Blueprint, render_template, flash, redirect, url_for, request

home_api = Blueprint('home_api', __name__, template_folder='templates')

@home_api.route("/")
def hello():
    return render_template('home.html')

