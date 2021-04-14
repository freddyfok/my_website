from my_website import app
"""
my_website is now a package
therefore it goes into __init__ and runs things there first
then it runs the following with app
"""


if __name__ == "__main__":
    app.run(debug=True)
