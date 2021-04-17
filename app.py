from flask import Flask, render_template, request, redirect, session, flash, url_for ,jsonify
from flask_login import login_required, current_user
from flask_dash_yaml.view import YamlDash,require_login


app = Flask(__name__)

CONFS=[	
		'app/teste.yaml',
		'app/teste2.yaml',
]

app.secret_key = '1ca308df6cdb0a8bf40d59be2a17eac1'
app.template_folder = 'templates'
app.static_folder='static'

dash=YamlDash()

dash.title('ShotoAuth')
dash.confs(CONFS)

dash.app(app)

app=dash.start()


@app.route('/users/<id>', methods=['GET'])
@app.route('/users', methods=['GET','POST'])
def users(id=-1):
	print(request.form)
	ret={}
	d = [{"id":0, "login":"John", "password":30, "group":"New York, teste, testes2","active":"false"},
		{"id":1 ,"login":"Fabio", "password":31, "group":"teste","active":"false"},
		{"id":2,"login":"Andrei", "password":31, "group":"New York","active":"true"},
		{"id":3,"login":"Fabio", "password":'2020-06-13', "group":"New York","active":"true"},
		{"id":4,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":5,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":6,"login":"Fabio", "password":31, "group":"New York","active":"false"},
		{"id":7,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":8,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":9,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":10,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":11,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":12,"login":"Fabio", "password":31, "group":"New York","active":"true"},
		{"id":13,"login":"Fabio", "password":31, "group":"New York","active":"true"}]
	if int(id) > -1:
		ret=jsonify(d[int(id)])
	else:
		ret=jsonify(d)
	return ret


@app.route('/groups/<id>', methods=['GET'])
@app.route('/groups', methods=['GET','POST'])
def groups(id=-1):
	print(request.form)
	ret={}
	d = [{"id":0,"group":"teste","active":"true"},{"id":1,"group":"New York","active":"false"}]
	if int(id) > -1:
		ret=jsonify(d[int(id)])
	else:
		ret=jsonify(d)

	return ret

if __name__ == "__main__":
	app.run(debug=True)
