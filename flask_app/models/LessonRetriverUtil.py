from flask.globals import request
from flask_app import app
from flask import flash, session
import re
import math
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


class Lesson:
    def __init__(self, data):
        self.info = []
    
    
    @classmethod
    def egg_lesson_info(cls,user):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 1 AND users_id = ({});".format(user) 
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 2 AND users_id = ({});".format(user)
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 3 AND users_id = ({});".format(user)
        query4 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 4 AND users_id = ({});".format(user)
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
    def pancake_lesson_info(cls,user):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 5 AND users_id = ({});".format(user)
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
    def meat_lesson_info(cls,user):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 6 AND users_id = ({});".format(user)
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 7 AND users_id = ({});".format(user)
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 8 AND users_id = ({});".format(user)
        query4 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 9 AND users_id = ({});".format(user)
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
    def starch_lesson_info(cls,user):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 10 AND users_id = ({});".format(user)
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 11 AND users_id = ({});".format(user)
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 12 AND users_id = ({});".format(user)
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
    def vegetable_lesson_info(cls,user):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 13 AND users_id = ({});".format(user)
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 14 AND users_id = ({});".format(user)
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
    def sauce_lesson_info(cls, user):
        query1 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 15 AND users_id = ({});".format(user)
        query2 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 16 AND users_id = ({});".format(user)
        query3 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 17 AND users_id = ({});".format(user)
        query4 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 18 AND users_id = ({});".format(user)
        query5 = "SELECT * FROM learntocook.pictures WHERE Lessons_id = 19 AND users_id = ({});".format(user)
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
    



