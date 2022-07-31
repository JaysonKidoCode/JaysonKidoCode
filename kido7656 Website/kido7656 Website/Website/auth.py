from flask import Blueprint

auth = Blueprint('views', _name_)


@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/Sign-Up')
def logout():
    return "<p>Sign Up</p>"
