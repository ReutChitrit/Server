import none
from flask import Flask, render_template, redirect, url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

app = Flask(__name__)



app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

###### Pages
## homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## ContactUs
from pages.ContactUs.ContactUs import ContactUs
app.register_blueprint(ContactUs)

## Assignment_4
from pages.Assignment_4.Assignment_4 import Assignment_4
app.register_blueprint(Assignment_4)

## Assignment3_1
from pages.Assignment3_1.Assignment3_1 import Assignment3_1
app.register_blueprint(Assignment3_1)

## Assignment3_2
from pages.Assignment3_2.Assignment3_2 import Assignment3_2
app.register_blueprint(Assignment3_2)


if __name__ == '__main__':
    app.run(debug=True)

    # reut