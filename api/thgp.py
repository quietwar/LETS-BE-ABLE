from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def form_info():
    return 'Welcome to my API/flask code'


@app.route('/submit', methods=["POST"])
def form_submit():
    f_user = request.form['']
    f_game = request.form['']
    f_games = request.form['']
    f_day = request.form['']
#return '' + '' + '' + ''

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
