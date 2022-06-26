from flask import render_template, Blueprint

ContactUs = Blueprint('ContactUs', __name__, static_folder='static',  static_url_path = '/pages/ContactUs', template_folder='templates')


@ContactUs.route('/contactus')
def go_to_contactus():
    return render_template('ContactUs.html')
