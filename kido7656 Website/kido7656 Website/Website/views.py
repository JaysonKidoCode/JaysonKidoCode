from flask import Blueprint, render_template

views = Blueprint('views', _name_)

@views.route('/')
def home():
    return render_template("home.html")