from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = '4d7c43d56bd44ced91c98799f6860a5e' # set a secret key for security purposes

@app.route('/') #get: see form
def show_counter():
    return render_template('show.html') #show html pg (don't use for method response)
        #template: use html in flask

@app.route('/count') #post: process form, send data
def create_counter():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return redirect('/')  #render show.html template


@app.route('/reset') #post: process form, send data
def reset():
    session.clear()
    session["counter"] = 1
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)



