import none
from flask import Flask, render_template, redirect, url_for
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/contactus')
def go_to_contactus():
    return render_template('Contact Us.html')


@app.route('/home')
def go_to_homepage():
    return render_template('homepage.html')


@app.route('/')
def redirect_homepage():
    return redirect(url_for('go_to_homepage'))


@app.route('/registerandsearch', methods=['GET', 'POST'])
def go_to_registerandsearch():
    if request.method == 'GET':
        if 'user_username' in request.args:
            user_username = request.args['user_username']
            if user_username in user_dict:
                return render_template('Assignment3_2.html',
                                       user_username=user_username,
                                       user_email=user_dict[user_username][0],
                                       user_age=user_dict[user_username][1])
            if len(user_username)==0:
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

@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))



user_dict = {
    'Rey': ['yo@gmail.com', '26'],
    'Lily': ['chill@gmail.com', '33'],
    'Harry': ['cool@gmail.com', '28'],
    'Ron': ['cookies@gmail.com', '34'],
    'Hermione': ['food@gmail.com', '23'],
    'Alon': ['yummycherries@gmail.com', '31'],
    'Dvir': ['smoothies@gmail.com', '27']
}


@app.route('/about')
def about_page():
    user_info = {'Name': 'Reut', 'Last Name': 'Chitrit', 'Nickname': 'Rey'}
    tv_characters = ('Jack Sparrow', 'Thomas Shelby', 'Ragnar Lothbrok', 'Khalisee')
    movies = ('Pirates of the Caribbean', 'Peaky Blinders', 'Vikings', 'Game of Throne')
    return render_template('Assignment3_1.html',
                           user_info=user_info, tv_characters=tv_characters,
                           movies=movies,
                           )


@app.route('/log_out')
def logout_func():
    session['registered'] = False
    session.clear()
    return redirect(url_for('go_to_registerandsearch'))