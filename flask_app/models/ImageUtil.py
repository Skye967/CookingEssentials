from flask.globals import request
from flask_app import app
from flask import flash
import re
import math
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

class Image:
    def __init__(self, data):
        self.info = []
        
        
    @classmethod
    def upload_image(cls,data ):
        query = "INSERT INTO `learntocook`.`pictures` (`picture`,`created_at`, `updated_at`, `users_id`, `Lessons_id`) VALUES (%(img_path)s, NOW(), NOW(), %(user_id)s, %(lesson_id)s);"
        user = connectToMySQL('learntocook').query_db(query,data)
        print(query)
        print(user)
        return user
    
    
    @classmethod
    def get_images(cls, user):
        query = "SELECT * FROM learntocook.pictures WHERE users_id = ({});".format(user)
        pictures_from_db = connectToMySQL("learntocook").query_db(query)
        return pictures_from_db
    
