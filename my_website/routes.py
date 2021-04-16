from flask import render_template
from my_website import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/wizard-score-sheet")
def wizard_calculator():
    return render_template("wizard-main.html")

#@app.route("/wizard-score-sheet/new-game")
