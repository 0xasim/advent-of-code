def parseFile(file_name):
	list_of_codes = []
	word = ""
	f = open(file_name, "r")
	lines_read = f.read()
	for each in lines_read:
		if each != ',':
			word+=each
		else:
			list_of_codes.append(word)
			word = ""

	list_of_codes.append('0')	#above loop missed last digit '0' because we are appending when comma is encountered and there is no comma after last digit
	ilo = []
	for each in list_of_codes:	#conversion into int
		ilo.append(int(each))
	return ilo

def solve_codes(code_list):
	i = 0
	while i <= len(code_list):
		#OPCODES
		first_value = code_list[i]
		#why check i+4 not i+3??
		if i+4<len(code_list):
			#noun
			sec_value = code_list[i+1]
			#verb
			third_value = code_list[i+2]
			fourth_value = code_list[i+3]
		#try first_value is 1 after solviing the memory problem
		if first_value is 1:
			code_list[fourth_value] = code_list[sec_value]+code_list[third_value]
		elif first_value is 2:
			code_list[fourth_value] = code_list[sec_value]*code_list[third_value]
		elif first_value is 99:
			break
		else:
			print("Encountering an unknown opcode. Something went wrong.")
		i+=4
	return code_list

ilo = parseFile("list_of_integers.txt")

def bruteforce_inputs():
	for noun in range(0,100):
		for verb in range(0,100):
			"""
			#https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list

			#you have to use .copy() method because simple using
			tempilo = ilo will create a variable tempilo but both
			refer to the same list, this is why challenge 
			mentioned multiple times to change memory after 
			every iteration
			"""
			tempilo = ilo.copy()

			tempilo[1] = noun
			tempilo[2] = verb

			result = solve_codes(tempilo)

			if result[0] == 19690720:
				print(f"Success on noun {noun} verb {verb}")
				print(noun*100+verb)
				return 0 #to break out of multiple loops

bruteforce_inputs()
