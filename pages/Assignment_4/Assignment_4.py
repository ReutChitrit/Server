import mysql
from flask import Blueprint, render_template, url_for, redirect, request, jsonify, session
import requests

Assignment_4 = Blueprint('Assignment_4', __name__, static_folder='static', static_url_path='/pages/Assignment_4',
                         template_folder='templates')


# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='mydb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #
@Assignment_4.route('/Assignment_4')
def go_to_Assignment_4():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('Assignment_4.html', users=users_list)


# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #
@Assignment_4.route('/insert', methods=['POST'])
def insert_user():
    name = request.form['username']
    email = request.form['email']
    age = request.form['age']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')
    # if letter_check(name):
    count = 0
    for user in users:
        if (name == user.name):
            count += 1

    if count == 0:
        query = "INSERT INTO users(name, email, age) VALUES ('%s', '%s', '%s')" % (name, email, age)
        interact_db(query=query, query_type='commit')
        query = 'select * from users'
        users_list = interact_db(query, query_type='fetch')
        return render_template('Assignment_4.html',
                               message='User has been added successfully.', users=users_list)
    else:
        return render_template('Assignment_4.html',
                               message='User already exists.', users=users)
    # return render_template('Assignment_4.html',
    #                                message='Please enter username containing only lowercase or uppercase letters.', users=users)


# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
@Assignment_4.route('/delete', methods=['POST'])
def delete_user():
    name = request.form['username']
    query = 'select * from users'
    users = interact_db(query, query_type='fetch')

    count = 0
    for user in users:
        if (name == user.name):
           count+=1

    if count==0:
        return render_template('Assignment_4.html',
                               message='User not found.', users=users)

    else:
        query = "DELETE FROM users WHERE name='%s';" % name
        interact_db(query, query_type='commit')

        query = 'select * from users'
        users_list = interact_db(query, query_type='fetch')

        return render_template('Assignment_4.html',
                               message='User has been deleted successfully.', users=users_list)



# ------------------------------------------------- #
# -------------------- UPDATE --------------------- #
# ------------------------------------------------- #
@Assignment_4.route('/update', methods=['POST'])
def update_user():
    name = request.form['username']
    email = request.form['email']
    age = request.form['age']

    query = 'select * from users'
    users = interact_db(query, query_type='fetch')

    count = 0
    for user in users:
        if (name == user.name):
           count+=1
           query = "UPDATE users SET email= '%s', age='%s' WHERE name='%s';" % (email, age, name)

           interact_db(query=query, query_type='commit')

           query = 'select * from users'
           users_list = interact_db(query, query_type='fetch')
           return render_template('Assignment_4.html',
                                  message='User has been updated successfully.', users=users_list)


    if count==0:
        return render_template('Assignment_4.html',
                               message='User not found.', users=users)






@Assignment_4.route('/Assignment_4/users')
def go_to_Assignment_4_jasonify():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)



@Assignment_4.route('/Assignment_4/outer_source')
def go_to_outer_source():
    user_id = request.args['user_id']
    response = requests.get(url=f"https://reqres.in/api/users/{user_id}")
    user = response.json()
    session['user'] = user.get('data')
    return render_template('Assignment_4.html')

def number_check(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

@Assignment_4.route('/Assignment_4/restapi_users', defaults={'USER_ID': 4})

@Assignment_4.route('/Assignment_4/restapi_users/<USER_ID>')
def print_restapi_user(USER_ID):
    if number_check(USER_ID):
        response = requests.get(url=f"https://reqres.in/api/users/{USER_ID}")
        if response.status_code is 200:
            users = response.json()
            return users.get('data')
        else:
            message = "User doesn't exist."
            return jsonify(message)
    else:
        message = "Please insert user ID."
        return jsonify(message)
