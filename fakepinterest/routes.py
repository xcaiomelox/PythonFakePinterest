#Aqui ficarão as rotas, os links do nosso site
from flask import render_template, url_for
from fakepinterest import app

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/profile/<user>")
def profile(user):
    return render_template("profile.html", user=user)