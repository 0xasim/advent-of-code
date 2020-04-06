#you need to find the intersection point closest to the central port.

def parse_file(file_name):
	with open(file_name,"r") as w:
		wires = w.readlines()

	all_wires = {}
	for wire_index, each_wire in enumerate(wires):          #two wires
		all_wires[wire_index] = each_wire.split(",")
	return all_wires

def convert_into_coordinates(all_wires):	#these are the coordinates
	all_grids = []
	total_distance = []
	for wire in all_wires:

		"""
		Not another way but the only way
		another way of doing this is by creating a matrix, initialize with some number e-g 7, map points belonging to a cables as their index (0,1 for two cables)
		map points of intersection as something (e-g 9) and then figure out to distances from points of intersection.
		It should work fine for small distances but when distance approaches 45762 
		then goodluck with creating (45762x45762) matrix. here is what numpy said:
		MemoryError: Unable to allocate 15.6 GiB for an array with shape (45762, 45762) and data type float64
		"""
		#initial position axis
		grid = [(0,0)]
		x, y = 0, 0	#at origin

		for each_point in all_wires[wire]:
			drc = each_point[0]		#direction
			dst = int(each_point[1:])	#distance

			if drc=="L":
				x -= dst	#change current position

			elif drc=="R":
				x += dst

			elif drc=="U":
				y += dst

			elif drc=="D":
				y -= dst
			else:
				print("direction not found")

			grid.append((x,y))
		all_grids.append(grid)
	return all_grids

def find_intersection(wires):
	intersect = []
	steps = []
	for i, ec0 in enumerate(wires[0]):		#ec = each coordinate
		if i  < len(wires[0])-1:
			cc0 = ec0
			nc0 = wires[0][i+1]
			if cc0[0] == nc0[0]:
				match_w0 = 0	#x-axis matched in wire 0
				unmatch_w0 = 1
			elif cc0[1] == nc0[1]:
				match_w0 = 1	#y-axis matched in wire 0
				unmatch_w0 = 0
			else:
				print("No coordinate matched in wire0")
			match_w0_value = cc0[match_w0]
			range_w0 = (cc0[unmatch_w0], nc0[unmatch_w0])
			for j, ec1 in enumerate(wires[1]):
				if j < len(wires[1])-1:
					cc1 = ec1
					nc1 = wires[1][j+1]
					#print(f"cc0:{cc0}, nc0:{nc0}, cc1:{cc1}, nc1:{nc1}")
					if cc1[0] == nc1[0]:
						match_w1 = 0	#x-axis matched in wire 1
						unmatch_w1 = 1
					elif cc1[1] == nc1[1]:
						match_w1 = 1	#y-axis matched in wire 1
						unmatch_w1 = 0
					else:
						print("No coordinate matched in wire1")
					match_w1_value = cc1[match_w1]
					range_w1 = (cc1[unmatch_w1], nc1[unmatch_w1])
					#print(f"range_w0: {range_w0}, range_w1: {range_w1}")
					#print(f"CC0 {cc0} : NC0{nc0} : CC1{cc1} : NC1{nc1}\n")
					#compare w0 match with w1 unmatch range
					if range_w1[0] < range_w1[1]:
						result = range_w1[0] <= match_w0_value <= range_w1[1]
					elif range_w1[0] > range_w1[1]:
						result = range_w1[0] >= match_w0_value >= range_w1[1]
					else:
						print("error range is equal")
					#print(result, end = ",")
					#print(f"COMPARE: {match_w0_value}, {range_w1}")
					
					if result:	#if same value is in range
						if range_w0[0] < range_w0[1]:
							result2 = range_w0[0] <= match_w1_value <= range_w0[1]
						elif range_w0[0] > range_w0[1]:
							result2 = range_w0[0] >= match_w1_value >= range_w0[1]
						else:
							print("error range is equal2")
						if result2:
							
							if not(match_w1 == match_w0):
								intersect.append(abs(match_w0_value) + abs(match_w1_value))
								if match_w0 == 0:
									steps.append(match_w0_value, match_w1_value)
								elif match_w0 == 1:
									steps.append(match_w1_value, match_w0_value)
							#print(f"range_w1: {range_w1}, match_w1_value: {match_w1_value}")
							#print(f"range_w0: {range_w0}, match_w0_value: {match_w0_value}")
							#print(f"cc0 {cc0} nc0 {nc0} cc1 {cc1} nc1 {nc1}\n")
	return intersect
def main():
	wp = parse_file("wire_paths.txt")
	grid = convert_into_coordinates(wp)
	intersect = find_intersection(grid)
	print(min(intersect))

if __name__ == "__main__":
	main()
