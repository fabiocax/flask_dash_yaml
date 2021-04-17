from flask import Flask, render_template, request, redirect, session, flash, url_for
from jinja2 import Environment, FileSystemLoader
import yaml
import json
from  flask_dash_yaml import components,functions
import importlib

try: 
	import constructor
except ModuleNotFoundError as error:
	print('erro')
APP=object()

def require_login(funcao):
	def wrapper(*args, **kwargs):
		#print(funcao.__name__)
		if not session.get('logged_in'):
			return render_template('login.html')
		else:
			return funcao(*args, **kwargs)	
	wrapper.__name__ = funcao.__name__	
	return wrapper


class LoadConfs(object):
	"""docstring for """
	def __init__(self,apps):
		self.apps=apps
		pass
	def reload(self):
		confs=[]
		try:
			importlib.reload(constructor)
			registry=constructor.CONSTRUTUOR_REGISTRY
			for makers in registry :
				yaml.add_constructor('!'+makers, registry[makers])
			for line in self.apps:
				with open(line) as f:
					yml=yaml.load(f, Loader=yaml.FullLoader)
					if yml['status']==True:
						confs.append(yml)
			return confs
		except:
			return confs		
##

class YamlDash(object):
	def __init__(self):
		pass
	
	def title(self,title='Dash'):
		self.title=title
	
	def confs(self,apps):
		self.load=LoadConfs(apps)
		self.confs=self.load.reload()

	def app(self,app):
		global APP
		self.app=app
		##Register functions from jinja2
		app.jinja_env.globals.update(clever_function=functions.clever_function)
		app.jinja_env.globals.update(find_string=functions.find_string)
		APP=app

	def auth(self,auth):
		self.login_required=auth

	def start(self):
		@self.app.route('/admin/static/<path:path>')
		def static_files(path):
			return self.app.send_static_file(path)

		@self.app.route('/admin/', methods=['GET'])
		@require_login
		def admin():
			return render_template('index.html'
				,title		=self.title
				,confs		=self.confs)


		@self.app.route('/admin/auth/login', methods=['GET','POST'])
		def login():
			if request.method == 'GET':
				session['logged_in'] = False
				pass
			if request.method == 'POST':
				login = request.form.get('login')
				password = request.form.get('password')
				session['logged_in'] = True
				return redirect('/admin/')

			return render_template('login.html'
				,title		=self.title
				,confs		=self.confs)

		@self.app.route('/admin/<appename>/<views>', methods=['GET'])
		@require_login
		def get_appname(appename,views):		
			template=components.get_template_view(self.confs,views,appename)
			return render_template(template+'/view.html'
				,title		= self.title
				,confs		= self.confs
				,view 		= views
				,appename	= appename
				,dataset 		= components.return_data_views(self.confs,appename,views))



		@self.app.route('/admin/<appename>/<views>/add/', methods=['GET','POST'])
		@require_login
		def get_appname_add(appename,views):
			if request.method == 'POST':
				components.post_data_dataset(self.confs,appename,views,request.form)
			itens   =components.get_columns_view(self.confs,views,appename)
			template=components.get_template_view(self.confs,views,appename)
			return render_template(template+'/add.html'
				,title		= self.title
				,confs		= self.confs
				,view 		= views
				,appename	= appename
				,itens		= components.serial_defaults_atributos_itens(itens)
				,dataset 	= components.return_data_views(self.confs,appename,views))





		@self.app.route('/admin/<appename>/<views>/<id>/change/', methods=['GET','POST'])
		@require_login
		def get_appname_change(appename,views,id):
			if request.method == 'POST':
				components.post_data_dataset(self.confs,appename,views,request.form)
			self.confs=self.load.reload()
			itens   =components.get_columns_view(self.confs,views,appename)
			template=components.get_template_view(self.confs,views,appename)
			return render_template(template+'/change.html'
				,title		= self.title
				,confs		= self.confs
				,view 		= views
				,appename	= appename
				,itens		= components.serial_defaults_atributos_itens(itens)
				,dataset 	= components.return_data_change(self.confs,appename,views,id))


		@self.app.route('/admin/<appename>/<views>/<id>/delete/', methods=['GET','POST'])
		@require_login
		def get_appname_delete(appename,views,id):
			template=components.get_template_view(self.confs,views,appename)
			return render_template(template+'/view.html'
				,title		= self.title
				,confs		= self.confs
				,view 		= views
				,appename	= appename
				,dataset 		= components.return_data_views(self.confs,appename,views))


		#FIM
		return self.app