from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def form_info():
	html_code =''
	html_code ='<form class="form-inline" role="form" method="POST" action="http://localhost:8888/submit"><div class="form-group">'
	html_code =''
	html_code =''
	html_code =''
	html_code =''
	html_code =''


	 close =  '</form>'
        return html_code +close

        @app.route('/submit', methods=["POST"])
def form_submit():
        f_user = request.form['']
        f_game = request.form['']
        f_games = request.form['']
        f_day = request.form['']

        return '' + '' + '' + ''

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
