from flask import Flask, request, redirect
app = Flask(__name__)

Look at your code and make sure the beginning of your form looks like this:

<form class="form-inline" role="form" method="POST" action="http://localhost:8888/submit">
	<div class="form-group">


Make a function like this:
@app.route('/submit', methods=['POST'])
def info():
	global info
	global data
	global scripture
	I1 = request.form['EmailInput1'] + "<br><br>"
	data = [{'Email':'%s'%(I1)}]
	info = json.dumps(data)
	scripture.write(info);
	return  redirect("http://localhost:8888/LETS - BE - ABLE/template.html", code=302)

Use request like this:
        I1 = request.form['(the name of your input)'] + '<br>'

        return all your variables