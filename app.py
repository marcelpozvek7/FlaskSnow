from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/o-meni")
def obout():
    return "<p>Zivjo sem Jan</p>"


app.run(debug = True)