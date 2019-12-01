import random
import sys

with open("input2.txt", 'w') as f:
	lines = []
	for x in range(int(sys.argv[1])):
		lines.append(f"{random.randint(0,1000)/100} {random.randint(0,1000)/100} {random.randint(1,5)} {random.randint(1,5)} {random.randint(1,5)}\n")
	f.writelines(lines)
