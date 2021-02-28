""" Docstring"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    """Docstring"""
    return render_template("home.html")
    # return "Site Homepage"


@app.route("/about/")
def about():
    """Docstring"""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
