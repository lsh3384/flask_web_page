from flask import Flask, render_template, url_for, request, redirect
import random, numpy, matplotlib
app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = request.form
        return render_template('home2.html', result=result)
    else:
        return render_template('home.html')


@app.route('/home2')
def user():
    return render_template('home2.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/')
def hello():
    return "Welcome home"


@app.route('/plus')
def plus():
    a = numpy.random.randint(11, 99, size=20)
    b = numpy.random.randint(11, 99, size=20)


    problem = []
    answer = []
    for a, b in zip(a, b):
        pro = str(a) + '+' + str(b)
        problem.append(pro)

        ans = format(a*b, ',')
        answer.append(ans)

    return render_template("plus.html", problem = problem, answer = answer)

@app.route('/minus')
def minus():
    return "minus"

@app.route('/multi')
def multi():

    a = numpy.random.randint(11, 99, size=20)
    b = numpy.random.randint(11, 99, size=20)


    problem = []
    answer = []
    for a, b in zip(a, b):
        pro = str(a) + ' X ' + str(b)
        problem.append(pro)

        ans = format(a*b, ',')
        answer.append(ans)

    return render_template("multi.html", problem = problem, answer = answer)

@app.route('/division')
def devision():
    return "division"


if __name__ == '__main__':
    app.run(debug='True')