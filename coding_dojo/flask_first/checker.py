from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("checker.html")	

@app.route('/<int:x>/<int:y>')
def change_color(x, y):
    return render_template("checker.html", x=x, y=y)	

if __name__=="__main__":
    app.run(debug=True)
    
    
    