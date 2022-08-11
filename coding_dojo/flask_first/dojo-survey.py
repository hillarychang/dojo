from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_keyy'

@app.route('/')
def show():
    return render_template('survey.html')

@app.route('/result')
def result():
    return render_template('survey-result.html')


@app.route('/info', methods=['POST']) #post: process form, send data
def process_info():
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_language'] = request.form['language']
    session['user_comments'] = request.form['comments']
    return redirect('/result') #use for post request



@app.route('/reset') 
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)