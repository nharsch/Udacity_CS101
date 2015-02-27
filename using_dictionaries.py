# Dictionaries

population = {
	"Shanghai" : 17.8,
	"Istabul" : 13.5,
	"Karachu" : 13.0,
	"Mumbai" : 12.5,
	"Brookyn" : 2.56,
	}

def dict_print(dict):
	for key in dict:
		print key, dict[key]

dict_print(population)
	
elements = {}
elements['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elements['He'] = {'name': 'Helium', 'number': 2, 'weight' : 'whatever'}

dict_print(elements)

