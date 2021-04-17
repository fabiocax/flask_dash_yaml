import json
import requests

def get_dataset(dataset):
	s = requests.Session()	
	r = s.get(dataset['GET'])
	return r.text

def post_dataset(dataset,data):
	s = requests.Session()	
	r = s.post(dataset['POST'], data = data)
	return r.text

def change_dataset(dataset,id):
	s = requests.Session()	
	r = s.get(dataset['GET_ID'].replace('{id}',str(id)))
	return r.text

def serial_defaults_atributos_itens(columns):
	serial={}
	for item in columns:
		its={}
		defaults={
			'type'			:'text',
			'visible'		:True,
			'sortable'		:False,
			'placeholder'	:'',
			'width'			:100,
			'list'			:True, 
			'values'		:{},
			'max_length'	:40,
			'index'			:False,
			'title'			:'noname'
		}

		for col in columns[item]:
			itemname=list(col)[0]
			try:
				del defaults[itemname]
			except:
				pass
			its.update(col)

		for defus in defaults:
			its.update({defus:defaults[defus]})
		serial[item]=its
	return serial

def post_data_dataset(confs,appename,views,data):

	dataset= get_dataset_view(confs,views,appename)
	post_dataset(dataset,data)


def return_data_views(confs,appename,views):
	its={}
	for app in confs:
		if appename ==app['appname']:
			dataset=get_dataset(app['views'][str(views)]['dataset'])
			colunas=serial_defaults_atributos_itens(app['views'][views]['columns'])
			for line in colunas:
				its.update({line:colunas[line]})
	return {'col':its,'dataset':json.loads(dataset)}


def return_data_change(confs,appename,views,id):
	its={}
	for app in confs:
		if appename ==app['appname']:
			dataset=change_dataset(app['views'][str(views)]['dataset'],id)
			colunas=serial_defaults_atributos_itens(app['views'][views]['columns'])
			for line in colunas:
				its.update({line:colunas[line]})
	return {'col':its,'dataset':json.loads(dataset)}


def get_template_view(conf,views,appename):
	template='default'
	for item in conf:
		if appename ==item['appname']:
			try:
				template=item['views'][views]['template']
			except:
				pass
	return template

def get_columns_view(conf,views,appename):
	itens='default'
	for item in conf:
		if appename ==item['appname']:
			try:
				itens=item['views'][views]['columns']
			except:
				pass
	return itens


def get_dataset_view(conf,views,appename):
	itens='default'
	for app in conf:
		if appename ==app['appname']:
			itens=app['views'][str(views)]['dataset']

	return itens


