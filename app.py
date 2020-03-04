# app.py
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("helloworld.html")


@app.route("/hello/<user>")
def hello_name(user):
    return render_template("hello.html", name=user)


@app.route("/passfail/<int:score>")
def passfail(score):
    return render_template("passfail.html", marks=score)


@app.route("/result")
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template("result.html", result=dict)


@app.route("/index")
def newindex():
    return render_template("index.html")


@app.route("/student", methods=['POST', 'GET'])
def student():
    return render_template("student.html")


@app.route("/studentresult", methods=['POST', 'GET'])
def studentresult():
    if request.method == 'POST':
        stdresult = request.form
        return render_template("table.html", result=stdresult)


@app.route("/success/<name>")
def success(name):
    return "Welcome " + name


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)
