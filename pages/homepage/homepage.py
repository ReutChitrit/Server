from flask import render_template, redirect, url_for, app, Blueprint

homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path = '/pages/homepage', template_folder='templates')

@homepage.route('/home')
def go_to_homepage():
    return render_template('homepage.html')


@homepage.route('/')
def redirect_homepage():
    return redirect(url_for('homepage.go_to_homepage'))


# fsdf