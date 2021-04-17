def clever_function():
    return u'HELLO'

def find_string(string,list):
	ret=False
	for line in list:
		if  string in line:
			ret= True
	return ret