import json

from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/submitty', methods=['POST'])
def Inputstuff():
	question2 = request.form['Whatsgoingon','oftenplace']
	if 'good' in question2: 
		return 'Success'
	else:
		return 'no'



if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')