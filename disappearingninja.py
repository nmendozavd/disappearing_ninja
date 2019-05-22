from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def nothing():
    return "No Ninjas Here"

@app.route('/ninja')
def ninja():
    return render_template('index.html', all_ninjas = True)

@app.route('/ninja/<ninja_color>')
def color(ninja_color):
    return render_template('index.html', all_ninjas = False, color = ninja_color)


app.run(debug=True)