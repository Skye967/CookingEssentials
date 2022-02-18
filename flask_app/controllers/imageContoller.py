from flask import render_template, redirect, request, session, flash, url_for
from flask_app import app
import os
from ..models.User import User
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

UPLOAD_FOLDER = './flask_app/static/img_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/upload/<int:lesson_id>", methods = ["POST","GET"])
def upload(lesson_id):
    path = "../static/img_uploads"
    print("Working")
    print(request.files)
    print(request.files['fileToUpload'])
    print(request.files['fileToUpload'].filename + "test")
    if request.method == "POST":
        if request.files['fileToUpload'].filename == '':
            print("testing")
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
            User.upload_picture(data)
            return redirect("/dashboard/display_images")
    return render_template("dashboard.html")


@app.route("/dashboard/display_images", methods = ["GET", "POST"])
def image_display():
    images = User.get_images(session['user_id'])
    eggs = User.egg_lesson_info()
    pancakes = User.pancake_lesson_info()
    meats = User.meat_lesson_info()
    starches = User.starch_lesson_info()
    vegetables = User.vegetable_lesson_info()
    sauces = User.sauce_lesson_info() 
    return render_template("dashboard.html", all_images = images, eggcompleted = eggs, pancakecompleted = pancakes, meatscompleted = meats, starchescompleted = starches, vegcompleted = vegetables, saucescompleted = sauces)


if __name__ == "__main__":
    app.run(debug=True)