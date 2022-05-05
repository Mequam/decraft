#add two sets together
def add_dictionary_vectors(d1,d2):
	for i in d1:
		if i in d2:	
			d2[i] += d1[i]
		else:
			d2[i] = d1[i]
	return d2

#scales a numeric set
def scale_dictionary_vectors(scalar,vector):
	for val in vector:
		vector[val] *= scalar
def dictionary_vector_str(v):
	ret_val = ''
	for k in v:
		ret_val += str(k) + ' : ' + str(v[k]) + '\n'
	return ret_val
		
def print_dictionary_vector(v):
	print(dictionary_vector_str(v))

#takes a crafting dictionary and returns a dictionary of 
#required materials
def decraft(craft_dictionary,item):		
	if item[1] in craft_dictionary:
		ret_val = {}
		for thing in craft_dictionary[item[1]]:
			add_dictionary_vectors(
				decraft(craft_dictionary,thing),
				ret_val
			)
		scale_dictionary_vectors(item[0],ret_val)
		return ret_val
	else:

		return {item[1]:item[0]}

if __name__:
	nms_crafting_dict = {
	"Mining Operation":[(2,"Solar Panel"),(2,"Batterie"),(1,"Extractor"),(2,"Supply Depot"),(2,"Supply Pipe")],
	"Solar Panel":[(1,"Metal Plating"),(30,"Gold"),(50,"Chromatic Metal")],
	"Batterie":[(60,"Magnatized Ferrite"),(100, "Condensed Carbon")],
	"Extractor":[(1,"Metal Plating"),(100,"Chromatic Metal")],
	"Supply Depot":[(10,"Metal Plating")],
	"Supply Pipe":[(25,"Ferrite Dust"),(10,"Carbon")]
	}
	
	print_dictionary_vector(decraft(nms_crafting_dict,(1,"Mining Operation")))
