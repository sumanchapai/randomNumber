#python file
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(0,100)
    return render_template("index.html", number = number)

if __name__ == '__main__':
    app.run(debug=True)
