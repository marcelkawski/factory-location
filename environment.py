import math
import random
from bee import Bee


class Environment:
	def __init__(self):
		self.resources = list()
		self.bees = list()
		self.min_x = self.min_y = 9999999999
		self.max_x = self.max_y = -999999999
		self.best_bee = None

	def get_input(self, file_name="input.txt"):
		with open(file_name) as f:
			for line in f:
				self.resources.append(list(map(float, line.split(" "))))

	def all_cost(self, factory_xy):
		all_cost = 0
		for source in self.resources:
			all_cost += source[4] * source[2] * (1 + math.tanh(source[3] * Environment.distance(factory_xy, (source[0], source[1]))))
		return all_cost

	def set_field(self):
		for source in self.resources:
			self.min_x = min(source[0], self.min_x)
			self.min_y = min(source[1], self.min_y)
			self.max_x = max(source[0], self.max_x)
			self.max_y = max(source[1], self.max_y)

	def add_bees(self, n):
		for i in range(n):
			b = Bee(x=random.randint(self.min_x*1000, self.max_x*1000)/1000, y=random.randint(self.min_y*1000, self.max_y*1000)/1000, env=self)
			self.bees.append(b)

	def algo11(self, omega, omega_min):
		for bee in self.bees:
			print(bee)
			bee.one_plus_one(omega=omega, omega_min=omega_min)
			print(bee, end="\n----------------\n")
			if (self.best_bee is None) or (bee.cost < self.best_bee.cost):
				self.best_bee = bee

	@staticmethod
	def distance(first, second):
		return math.sqrt((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2)
