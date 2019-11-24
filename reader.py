import math


def get_input(file_name):
	result = list()
	with open(file_name) as f:
		for line in f:
			result.append(list(map(int, line.split(" "))))
	return result


def distance(first, second):
	return math.sqrt((first[0]-second[0])**2 + (first[1]-second[1])**2)


def single_cost(factory_xy, source):
	return source[4] * source[2] * (1 + math.tanh(source[3] * distance(factory_xy, (source[0], source[1]))))


def all_cost(factory_xy, resources):
	cost = 0
	for source in resources:
		#  cost += single_cost(factory_xy=factory_xy, source=source)
		cost += source[4] * source[2] * (1 + math.tanh(source[3] * distance(factory_xy, (source[0], source[1]))))
	return cost


res = get_input(file_name="input.txt")

for x in range(-50, 50):
	print(f"{x}: {all_cost((x,0), res)}")
