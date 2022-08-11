from flask import Flask, render_template, request, redirect, session
import random  # import the random module

app = Flask(__name__)
app.secret_key = '4d7c43d56bd44ced91c98799f6860a5e' # set a secret key for security purposes


@app.route('/') #get: see form
def show():
    if 'true_num' not in session:
        session['true_num']  = random.randint(1, 100) 		# random number between 1-100
    return render_template('numgame.html') #show html pg (don't use for method response)
        #template: use html in flask



@app.route('/guess', methods=['POST']) #post: process form, send data
def process_guess():
    # Here we add a property to session to store the name 
    session['user_guess'] = int(request.form['guess'])
    return redirect('/') #use for post request



@app.route('/reset') #post: process form, send data
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)