from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/ping")
def ping(name="tskxz"):
    return render_template("ping.html", person=name)