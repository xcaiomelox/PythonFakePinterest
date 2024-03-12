#Aqui ficarão as rotas, os links do nosso site
from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCreateAccount

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
    formcreateaccount = FormCreateAccount()
    return render_template("createaccount.html", form=formcreateaccount)

@app.route("/profile/<user>")
@login_required
def profile(user):
    return render_template("profile.html", user=user)