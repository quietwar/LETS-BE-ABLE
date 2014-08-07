import json

from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def Join_Now():
	data = open("data.txt", "a+")
	z = request.form['appproblem'] 
	ze = request.form['changeapp'] 
	zeb = request.form['tellapp'] 

	k = [{'appproblem':(z)}, {'changeapp':(ze)}, {'tellapp':(zeb)}]
	info = json.dumps(k)
	data.write(info);
	data.close()
	return redirect("http://localhost:8888/LETS-BE-ABLE/template5.html", code=302)


@app.route('/submity', methods=['POST'])
def speak_up():
	data = open("data.txt", "a+")
	name = request.form['nameform']
	mail = request.form['emailform']
	message = request.form['messageform']

	kay = [{'nameform':(name)}, {'emailform':(mail)}, {'messageform':(message)}]
	info = json.dumps(k)
	data.write(info);
	data.close()
	return redirect("http://localhost:8888/LETS-BE-ABLE/template6.html", code=302)



@app.route('/submitty', methods=['POST'])
def why_now():
	data = open("data.txt", "a+")
	question1 = request.form['parentask']
	question2 = request.form['Whatsgoingon']
	question4 = request.form['oftenplace']
	question5 = request.form['zae9']
	question6 = request.form['zae10']
	question7 = request.form['zae11']
	question8 = request.form['zae12']
	question9 = request.form['zae13']
	question10 = request.form['zae14']

	question_dic = {'question1':question1,'question2' :question2 , 'question4':question4 , 'question5':question5, 'question6':question6, 'question7':question7, 'question8':question8 , 'question9':question9, 'question10':question10}
	info = json.dumps(question_dic)
	data.write(info);
	data.close()
	return redirect("http://localhost:8888/LETS-BE-ABLE/template.html", code=302)



if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')

