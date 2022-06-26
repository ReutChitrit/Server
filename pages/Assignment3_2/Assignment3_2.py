from flask import request, render_template, app, session, jsonify, Blueprint, url_for, redirect

Assignment3_2 = Blueprint('Assignment3_2', __name__, static_folder='static',  static_url_path = '/pages/Assignment3_2', template_folder='templates')


@Assignment3_2.route('/registerandsearch', methods=['GET', 'POST'])
def go_to_registerandsearch():
    if request.method == 'GET':
        if 'username' in request.args:
            username = request.args['username']
            if username in user_dict:
                return render_template('Assignment3_2.html',
                                       username=username,
                                       email=user_dict[username][0],
                                       age=user_dict[username][1])
            if len(username)==0:
                return render_template('Assignment3_2.html',
                                       user_dict=user_dict)
            else:
                return render_template('Assignment3_2.html',
                                       message='User not found.')

    if request.method == 'POST':
        reg_username = request.form['username']
        reg_email = request.form['email']
        reg_age = request.form['age']
        session['username'] = reg_username
        session['email'] = reg_email
        session['age'] = reg_age
        session['registered'] = True
        return render_template('Assignment3_2.html')

    return render_template('Assignment3_2.html')

@Assignment3_2.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))

@Assignment3_2.route('/log_out')
def logout_func():
    session['registered'] = False
    session.clear()
    return redirect(url_for('Assignment3_2.go_to_registerandsearch'))


user_dict = {
    'Rey': ['yo@gmail.com', '26'],
    'Lily': ['chill@gmail.com', '33'],
    'Harry': ['cool@gmail.com', '28'],
    'Ron': ['cookies@gmail.com', '34'],
    'Hermione': ['food@gmail.com', '23'],
    'Alon': ['yummycherries@gmail.com', '31'],
    'Dvir': ['smoothies@gmail.com', '27']
}