import math

def calculate_fuel(mass):       #mass can be fuel mass or modue mass
	if(mass>0):
		#round down, not round off
		fuel = (math.floor(mass/3))-2

		if(fuel>0):	#fuel drops below zero in the end which results in incorrect value
			#recursion
			return fuel + calculate_fuel(fuel)
		else:	#why nonetype error
			return 0

f = open("module_masses.txt", "r")
modules = f.readlines()
total_fuel = 0
for eachmodule in modules:
	module_mass = int(eachmodule)
	total_fuel += calculate_fuel(module_mass)

print(total_fuel)
f.close()
