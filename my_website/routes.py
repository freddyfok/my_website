from flask import render_template
from my_website import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/score-sheets")
def score_sheet():
    return render_template("score-sheets-main.html")


@app.route("/score-sheets/wizard")
def wizard_score_sheet():
    return render_template("wizard.html")
