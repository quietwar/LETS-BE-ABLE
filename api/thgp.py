#support
from flask import Flask,request,json
app = Flask(__name__)

@app.route("/")
def form_info():
    return 'Welcome to my API/flask code'

@app.route('/submit', methods=["POST"])
def form_submit():
	z_problem = request.form['appproblem']
	Change_app = request.form['changeapp']
	tell_app = request.form['tellapp']
	return  z_problem  + ' ' + Change_app + ' ' +  tell_app 

########################

@app.route('/submity', methods=['POST'])
def contactform():
    name = request.form['nameform']
    mail = request.form['emailform']
    message = request.form['messageform']

    contact_dict = {'name':name,'mail': mail, 'message':message}
    contact_json = json.dumps(contact_dict)
    return contact_json

####################################



@app.route('/submitty', methods=['POST'])
def Questionform():
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
    question_json = json.dumps(question_dic)
    print "\t\t question_json = %s" % question_json
    return question_json 
    
if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')