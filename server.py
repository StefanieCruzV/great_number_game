from crypt import methods
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'page'


@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randint(1, 100)
        print(session['random'])
    if 'tries' not in session:
        session['tries'] = 0
    return render_template("index.html")


@app.route('/guess', methods=['post'])
def guess():
    htmltext = ""
    color = "bg-danger"
    hidden= "hidden"
    session['tries'] = session['tries']+1
    print(session['tries'])
    print(request.form["number"])
    if session['tries'] >= 5:
        return redirect("/reset")
    if int(request.form['number']) == session['random']:
        htmltext = "You Guessed it!! The number was " + \
            str(session['random'])
        color = "bg-success"
        hidden=""
    elif int(request.form['number']) > session['random']:
        htmltext = "Too High!"
    else:
        htmltext = "Too low!"
    return render_template("guess.html", htmltexthtml=htmltext, color=color, tries= session['tries'],hidden =hidden)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
