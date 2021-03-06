from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/colors")
def colors():
    return render_template("colors.html")


@app.route("/blue")
def blue():
    return render_template("colors.html", color="blue")


@app.route("/red")
def red():
    return render_template("colors.html", color="red")


@app.route("/green")
def green():
    return render_template("colors.html", color="green")


@app.route("/yellow")
def yellow():
    return render_template("colors.html", color="yellow")


if __name__ == "__main__":
    app.run(debug=True, port=8081)
