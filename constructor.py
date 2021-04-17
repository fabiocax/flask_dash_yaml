

def constructor(loader, node) :
    fields = loader.construct_mapping(node)
    return {'teste44': 'teste','New York': 'New York','testes':'dds','testes2':'dds','testes6':'dds2'}



def constructor2(loader, node) :	
	return {'teste2': 'teste','New York': 'New York','testes':'dds','testes8':'dds','testes7':'dds2'}



##Not Remove
CONSTRUTUOR_REGISTRY={
	'Test':constructor,
	'Test2':constructor2,


	}