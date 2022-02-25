from flask import render_template, redirect, request, session, flash, url_for
from flask_app import app
import os
from ..models.User import User
from ..models.LessonRetriverUtil import Lesson
from ..models.ImageUtil import Image
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

UPLOAD_FOLDER = './flask_app/static/img_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/upload/<int:lesson_id>", methods = ["POST","GET"])
def upload(lesson_id):
    path = "../static/img_uploads"
    if request.method == "POST":
        if request.files['fileToUpload'].filename == '':
            print(request.url)
            return redirect("/index")
        print(request.files['fileToUpload'])
        if request.files:
            image = request.files['fileToUpload']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            print("save image")
            img_path = path +"/"+ image.filename
            data = {
                'lesson_id': lesson_id,
                'user_id': session['user_id'],
                'img_path': img_path
            }
            Image.upload_image(data)
            return redirect("/dashboard/display_images")
    return render_template("dashboard.html")


@app.route("/dashboard/display_images", methods = ["GET", "POST"])
def image_display():
    images = Image.get_images(session['user_id'])
    eggs = Lesson.egg_lesson_info(session['user_id'])
    pancakes = Lesson.pancake_lesson_info(session['user_id'])
    meats = Lesson.meat_lesson_info(session['user_id'])
    starches = Lesson.starch_lesson_info(session['user_id'])
    vegetables = Lesson.vegetable_lesson_info(session['user_id'])
    sauces = Lesson.sauce_lesson_info(session['user_id']) 
    return render_template("dashboard.html", all_images = images, eggcompleted = eggs, pancakecompleted = pancakes, meatscompleted = meats, starchescompleted = starches, vegcompleted = vegetables, saucescompleted = sauces)


if __name__ == "__main__":
    app.run(debug=True)