import datetime
from flask import Flask


app = Flask(__name__)


@app.route("/")
def main():
    current_date = datetime.date.today()
    return str(current_date)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
