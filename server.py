from flask_app import app
# from flask_app.controllers import tv_controller
from flask_app.controllers import imageContoller
from flask_app.controllers import lessonController
from flask_app.controllers import userController
from flask_app.config.my_sequal_connections import connectToMySQL


if __name__ == "__main__":
    app.run(debug=True)