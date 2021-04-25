from flask import render_template
from my_website import app

LINKEDIN_LINK = "https://www.linkedin.com/in/freddyfok/"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", linkedin_link=f"{LINKEDIN_LINK}")


@app.route("/score-sheets")
def score_sheet():
    return render_template("score-sheets-main.html")


@app.route("/score-sheets/new-wizard")
def wizard_score_sheet():
    return render_template("wizard.html")
