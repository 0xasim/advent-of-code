import math
total_fuel = 0
f = open("module_masses.txt", "r")
modules = f.readlines()
for eachmodule in modules:
	module_mass = int(eachmodule)
	#round down, not round off
	module_fuel = math.floor((module_mass/3))-2
	total_fuel+=module_fuel
print(total_fuel)
f.close
