from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/1")
def page1():
    return render_template("page1.html")


@app.route("/2")
def page2():
    return render_template("page2.html")


if __name__ == "__main__":
    app.run(debug=True)
