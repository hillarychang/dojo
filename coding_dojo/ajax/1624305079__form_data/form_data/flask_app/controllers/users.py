from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())


@app.route('/create/user',methods=['POST'])
def create_user():
    
    data = {
        "user_name": request.form['uname'],
        "email": request.form['email']
    }

    user_id = User.save(data)
    return jsonify(message="Add a user!!!")



