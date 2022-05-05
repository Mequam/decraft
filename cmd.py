import decraft
#this is the command interface for the decrafting code

def isNum(x):
	try:
		return int(x)
	except:
		return False
#takes an array of strings and returns an array of tupples taged with numbers
def getItemVector(args):
	ret_val = []
	carry_str = ''
	last_number = 0
	for i in args:
		x = isNum(i)
		if x:
			if last_number != 0:
				ret_val.append((x,carry_str[:-1]))
			carry_str = ''
			last_number = x
		else:
			carry_str += i + ' '
	ret_val.append((last_number,carry_str[:-1]))
	return ret_val			
			
#takes an array of strings and returns a decrafted dictionary
#this is inteanded to be used when the crafting dictionary is already known

def decraftArgs(craft_dict,args):
	ret_val = {}
	for item in getItemVector(args):	
		decraft.add_dictionary_vectors(decraft.decraft(craft_dict,item),ret_val)
	return ret_val

if __name__ == '__main__':
	import sys
	
	nms_crafting_dict = {
	"Mining Operation":[(2,"Solar Panel"),(2,"Batterie"),(1,"Extractor"),(2,"Supply Depot"),(2,"Supply Pipe")],
	"Solar Panel":[(1,"Metal Plating"),(30,"Gold"),(50,"Chromatic Metal")],
	"Batterie":[(60,"Magnatized Ferrite"),(100, "Condensed Carbon")],
	"Extractor":[(1,"Metal Plating"),(100,"Chromatic Metal")],
	"Supply Depot":[(10,"Metal Plating")],
	"Supply Pipe":[(25,"Ferrite Dust"),(10,"Carbon")]
	}
	decraft.print_dictionary_vector(decraftArgs(nms_crafting_dict,sys.argv[1:]))

