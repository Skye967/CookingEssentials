from flask import render_template, redirect, request, session, flash, url_for
from flask_app import app
import os
from ..models.User import User
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/egg")
def egg_less():
    return render_template("egglesson.html")


@app.route("/egg/scrambled")
def scrambled_egg():
    return render_template("scrambledegg.html")


@app.route("/egg/overeasy")
def overeasy_egg():
    return render_template("overeasy.html")


@app.route("/egg/hardboiled")
def hardboiled_egg():
    return render_template("hardboiled.html")


@app.route("/egg/poached")
def pancake():
    return render_template("poached.html")

@app.route("/pancake")
def poached_egg():
    return render_template("pancake.html")


@app.route("/meat")
def meat():
    return render_template("meat_lesson.html")


@app.route("/meat/chicken")
def chicken():
    return render_template("chicken.html")


@app.route("/meat/steak")
def steak():
    return render_template("steak.html")


@app.route("/meat/pork")
def pork():
    return render_template("pork.html")


@app.route("/meat/fish")
def fish():
    return render_template("fish.html")


@app.route("/starch")
def starch():
    return render_template("starch.html")


@app.route("/starch/potatoe")
def potatoe():
    return render_template("potatoe.html")


@app.route("/starch/rice")
def rice():
    return render_template("rice.html")


@app.route("/starch/pasta")
def pasta():
    return render_template("pasta.html")


@app.route("/vegetable")
def vegetable():
    return render_template("vegetable.html")


@app.route("/vegetable/saute")
def sauteveggie():
    return render_template("sauteveggie.html")


@app.route("/vegetable/boil")
def boilveggie():
    return render_template("boilveggie.html")


@app.route("/saucey")
def saucey():
    return render_template("saucey.html")


@app.route("/saucey/veloute")
def veloute():
    return render_template("veloute.html")


@app.route("/saucey/pansauce")
def pansauce():
    return render_template("pansauce.html")


@app.route("/saucey/tomotoe")
def tomatoe():
    return render_template("tomatoesauce.html")


@app.route("/saucey/balsamic")
def balsamic():
    return render_template("balsamic.html")


@app.route("/saucey/hollandaise")
def hollandaise():
    return render_template("hollandaise.html")


if __name__ == "__main__":
    app.run(debug=True)