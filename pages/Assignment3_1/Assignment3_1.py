from flask import render_template, Blueprint

Assignment3_1 = Blueprint('Assignment3_1', __name__, static_folder='static', static_url_path = '/pages/Assignment3_1', template_folder='templates')

@Assignment3_1.route('/about')
def about_page():
    user_info = {'Name': 'Reut', 'Last Name': 'Chitrit', 'Nickname': 'Rey'}
    tv_characters = ('Jack Sparrow', 'Thomas Shelby', 'Ragnar Lothbrok', 'Khalisee')
    movies = ('Pirates of the Caribbean', 'Peaky Blinders', 'Vikings', 'Game of Throne')
    return render_template('Assignment3_1.html',
                           user_info=user_info, tv_characters=tv_characters,
                           movies=movies,
                           )

