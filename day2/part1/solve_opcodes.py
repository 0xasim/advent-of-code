"""
#first digit(position 0) is opcode telling what to do and everything else is a position for one pair.
#position of values at 1 and 2 are to which opcode applies and stored at position indicated
#by element 3
#integers indicate position of values not values themselves
"""

ilo = []

def parseFile(file_name):
	list_of_codes = []
	word = ""
	f = open(file_name, "r")
	lines_read = f.read()
	for each in lines_read:
		if each!=',':
			word+=each
		else:
			list_of_codes.append(word)
			word = ""

	list_of_codes.append('0')	#above loop missed last digit '0' because we are appending when comma is encountered and there is no comma after last digit
	global ilo	#int_list_of_integers
	for each in list_of_codes:	#conversion into int
		ilo.append(int(each))

def solve_codes(code_list):
	i = 0
	while i <= len(code_list):
		#OPCODES
		first_value = code_list[i]
		
		if(i+4<=len(code_list)):
			sec_value = code_list[i+1]
			third_value = code_list[i+2]
			fourth_value = code_list[i+3]
		
		if(first_value==1):
			code_list[fourth_value] = code_list[sec_value]+code_list[third_value]
		elif(first_value==2):
			code_list[fourth_value] = code_list[sec_value]*code_list[third_value]
		elif(first_value==99):
			break
		else:
			print("No case matched --problem--problem--")
		i+=4
	return code_list

parseFile("list_of_integers.txt")
#inputs
ilo[1] = 12
ilo[2] = 2

print(solve_codes(ilo))
