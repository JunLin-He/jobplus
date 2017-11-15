from flask import Blueprint, render_template, redirect, url_for


front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')
