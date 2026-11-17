from flask import Flask, render_template
import random 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/o-meni")
def obout():
    return render_template("about.html")

#met kocke... rabdom (1-N)
@app.route("/kocka/<N>")
def kocka(N):
    rng=(random.randint(1,int(N)))
    print(rng)
    return render_template("kocka.html", kocka = rng)


@app.route("/kocka/<N>")
def love(N):
    rng=(random.randint(1,int(N)))
    print(rng)
    return render_template("love.html", kocka = rng)

sez = [1,2,3]
print(random.choice(sez))




app.run(debug = True)