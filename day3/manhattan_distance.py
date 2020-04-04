import numpy as np
#you need to find the intersection point closest to the central port.

def parse_file(file_name):
	with open(file_name,"r") as w:
		wires = w.readlines()

	#who else loves data parsing?
	all_wires = {}
	for wire_index, each_wire in enumerate(wires):          #two wires
		all_wires[wire_index] = each_wire.split(",")
	return all_wires

def calc_shortest_dist(grid):
	aa = []
	for ci, cable in enumerate(grid):
		a = []
		for cpi, coordinate_point in enumerate(cable):
			if cpi < len(cable)-1:
				current_coordinate = coordinate_point
				next_coordinate = cable[cpi+1]
				#print(f"current: {current_coordinate},next: {next_coordinate}")

				if current_coordinate[0] == next_coordinate[0]:
					#value = current_coordinate[0]
					if current_coordinate[1] < next_coordinate[1]:
						for i in range(current_coordinate[1], next_coordinate[1]):
							a.append((current_coordinate[0],i))
					else:
						for i in range(next_coordinate[1],current_coordinate[1]):
							a.append((current_coordinate[0],i))
				elif current_coordinate[1] == next_coordinate[1]:
					if current_coordinate[0] < next_coordinate[0]:
						for i in range(current_coordinate[0], next_coordinate[0]):
							a.append((i,current_coordinate[0]))
					else:
						for i in range(next_coordinate[0],current_coordinate[0]):
							a.append((i,current_coordinate[0]))
				else : print("coordinates donot match")
		aa.append(a)
	return aa

def map_on_grid(all_wires):	#these are the coordinates
	all_grids = []
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
		grid = []
		x, y = 0, 0	#at origin

		for each_point in all_wires[wire]:
			drc = each_point[0]		#direction
			dst = int(each_point[1:])	#distance

			if drc=="L":
				x -= dst	#change current position

			elif drc=="R":
				x += dst

			elif drc=="U":
				y -= dst

			elif drc=="D":
				y += dst

			grid.append((x,y))
		all_grids.append(grid)

	return all_grids

def main():
	wp = parse_file("example.txt")
	grid = map_on_grid(wp)
	for each in grid:
		print(each)
	calc_shortest_dist(grid)

if __name__ == "__main__":
	main()
