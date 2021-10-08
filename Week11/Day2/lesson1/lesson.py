from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/in-this-chapter")
def lesson():
    contant = open('in-this-chapter.md', 'r').read()
    return render_template_string(contant)


@app.route("/exercise")
def exercise():
    contant = open('exercises.md', 'r').read()
    return render_template_string(contant)


if __name__ == "__main__":
    app.run(debug=True)
