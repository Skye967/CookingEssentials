from flask.globals import request
from flask_app import app
from flask import flash
import re
import math
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

PASSWORD_REGEX = re.compile(r'\A(?=\S*?\d)(?=\S*?[A-Z])(?=\S*?[a-z])\S{6,}\Z')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.ename = data['email']
        self.fname = data['first_name']
        self.lname = data['last_name']
        self.password = data['pword']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.emails = []
        self.info = []
    
    
    @classmethod
    def user_login(cls,data):
        login_query = "SELECT * FROM learntocook.users WHERE email = %(login)s;"
        login_pword = data['pass']
        pword = "SELECT pword FROM learntocook.users WHERE email = %(login)s;"  
        user_id1 = connectToMySQL('learntocook').query_db(login_query,data)
        passwords = connectToMySQL('learntocook').query_db(pword,data)
        table1 = []
        print(user_id1)
        if user_id1 == ():
            flash("Invalid login or password!")
            return False
        for info in user_id1:
            table1.append(cls(info))
        if(bcrypt.check_password_hash(passwords[0]['pword'], login_pword) == False):
            return False
        return table1
    

    @classmethod
    def add_email(cls,data):
        query = "INSERT INTO learntocook.users (first_name, last_name, email, pword, updated_at, created_at) VALUES (%(firstname)s, %(lastname)s, %(email_name)s, %(p_word)s, NOW(), NOW());"
        user_id = connectToMySQL('learntocook').query_db(query,data)
        return user_id  
    
     
    @staticmethod
    def validate_email( user ):
        is_valid = True
        ename = (user['email_name'])
        if not EMAIL_REGEX.match(user['email_name']): 
            flash("Invalid email address!")
            is_valid = False
        if not user['firstname'].isalpha():
            flash("Invalid first name!")
            is_valid = False
        if not user['lastname'].isalpha():
            flash("Invalid last name!")
            is_valid = False
        if  EMAIL_REGEX.match(user['email_name']): 
            flash(f"The email that you have entered {ename} is a valid email adress!")
            is_valid = True 
        if user['p_word'] != user['password_confirmation']:
            flash("invalid password confirmation!")
            is_valid = False
        if not PASSWORD_REGEX.match(user['p_word']):
            flash("invalid password!")
            is_valid = False
        return is_valid