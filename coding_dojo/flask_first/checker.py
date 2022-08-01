from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/play')
# def index():
#     return render_template("index.html")	

@app.route('/play/<int:x>/<int:y>')
def change_color(x, y):
    return render_template("checker.html", x=x, y=y)	

if __name__=="__main__":
    app.run(debug=True)
    
    
    