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
    def upload_picture(cls,data ):
        query = "INSERT INTO `learntocook`.`pictures` (`picture`,`created_at`, `updated_at`, `users_id`, `Lessons_id`) VALUES (%(img_path)s, NOW(), NOW(), %(user_id)s, %(lesson_id)s);"
        user = connectToMySQL('learntocook').query_db(query,data)
        print(query)
        print(user)
        return user
    
    
        
        
        
    @classmethod
    def display_emails(cls):
        query = "SELECT * FROM learntocook.users;"
        emails_from_db = connectToMySQL("learntocook").query_db(query)
        emails = [] 
        for email in emails_from_db:
            emails.append(cls(email)) 
        return emails
    
    
    @classmethod
    def egg_lesson_info(cls):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 1;"
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 2;"
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 3;"
        query4 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 4;"
        lesson_from_db = connectToMySQL("learntocook").query_db(query1)
        lesson_from_db2 = connectToMySQL("learntocook").query_db(query2)
        lesson_from_db3 = connectToMySQL("learntocook").query_db(query3)
        lesson_from_db4 = connectToMySQL("learntocook").query_db(query4)
        sum = 0
        if lesson_from_db == ():
            query1 = 0
        else: query1 = 1
        if lesson_from_db2 == ():
            query2 = 0
        else: query2 = 1
        if lesson_from_db3 == ():
            query3 = 0
        else: query3 = 1
        if lesson_from_db4 == ():
            query4 = 0
        else: query4 = 1
        sum = query1 + query2 + query3 + query4
        results = math.floor(sum / 4 * 100)
        complete = str(results) + "%" 
        return complete
    
    
    @classmethod
    def pancake_lesson_info(cls):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 5;"
        lesson_from_db = connectToMySQL("learntocook").query_db(query1)
        sum = 0
        if lesson_from_db == ():
            query1 = 0
        else: query1 = 1
        sum = query1
        results = math.floor(sum / 1 * 100)
        complete = str(results) + "%" 
        return complete
    
    
    @classmethod
    def meat_lesson_info(cls):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 6;"
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 7;"
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 8;"
        query4 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 9;"
        lesson_from_db = connectToMySQL("learntocook").query_db(query1)
        lesson_from_db2 = connectToMySQL("learntocook").query_db(query2)
        lesson_from_db3 = connectToMySQL("learntocook").query_db(query3)
        lesson_from_db4 = connectToMySQL("learntocook").query_db(query4)
        sum = 0
        if lesson_from_db == ():
            query1 = 0
        else: query1 = 1
        if lesson_from_db2 == ():
            query2 = 0
        else: query2 = 1
        if lesson_from_db3 == ():
            query3 = 0
        else: query3 = 1
        if lesson_from_db4 == ():
            query4 = 0
        else: query4 = 1
        sum = query1 + query2 + query3 + query4
        results = math.floor(sum / 4 * 100)
        complete = str(results) + "%" 
        return complete
    
    
    @classmethod
    def starch_lesson_info(cls):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 10;"
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 11;"
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 12;"
        lesson_from_db = connectToMySQL("learntocook").query_db(query1)
        lesson_from_db2 = connectToMySQL("learntocook").query_db(query2)
        lesson_from_db3 = connectToMySQL("learntocook").query_db(query3)
        sum = 0
        if lesson_from_db == ():
            query1 = 0
        else: query1 = 1
        if lesson_from_db2 == ():
            query2 = 0
        else: query2 = 1
        if lesson_from_db3 == ():
            query3 = 0
        else: query3 = 1
        sum = query1 + query2 + query3
        results = math.floor(sum / 3 * 100)
        complete = str(results) + "%" 
        return complete
    
    
    @classmethod
    def vegetable_lesson_info(cls):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 13;"
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 14;"
        lesson_from_db = connectToMySQL("learntocook").query_db(query1)
        lesson_from_db2 = connectToMySQL("learntocook").query_db(query2)
        sum = 0
        if lesson_from_db == ():
            query1 = 0
        else: query1 = 1
        if lesson_from_db2 == ():
            query2 = 0
        else: query2 = 1
        sum = query1 + query2
        results = math.floor(sum / 2 * 100)
        complete = str(results) + "%" 
        return complete
    
    
    @classmethod
    def sauce_lesson_info(cls):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 15;"
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 16;"
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 17;"
        query4 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 18;"
        query5 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 19;"
        lesson_from_db = connectToMySQL("learntocook").query_db(query1)
        lesson_from_db2 = connectToMySQL("learntocook").query_db(query2)
        lesson_from_db3 = connectToMySQL("learntocook").query_db(query3)
        lesson_from_db4 = connectToMySQL("learntocook").query_db(query4)
        lesson_from_db5 = connectToMySQL("learntocook").query_db(query4)
        sum = 0
        if lesson_from_db == ():
            query1 = 0
        else: query1 = 1
        if lesson_from_db2 == ():
            query2 = 0
        else: query2 = 1
        if lesson_from_db3 == ():
            query3 = 0
        else: query3 = 1
        if lesson_from_db4 == ():
            query4 = 0
        else: query4 = 1
        if lesson_from_db5 == ():
            query5 = 0
        else: query5 = 1
        sum = query1 + query2 + query3 + query4 + query5
        results = math.floor(sum / 5 * 100)
        complete = str(results) + "%" 
        return complete
    
    
    @classmethod
    def get_images(cls, user):
        query = "SELECT * FROM learntocook.pictures WHERE users_id = ({});".format(user)
        pictures_from_db = connectToMySQL("learntocook").query_db(query)
        return pictures_from_db
    
    
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