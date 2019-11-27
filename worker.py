from random import normalvariate
from reader import all_cost


class Bee:
	def __init__(self, x, y, env):
		self.x = x
		self.y = y
		self.env = env

	def next_step(self, omega):
		x_, y_ = (self.x+omega*normalvariate(0, 1), self.y+omega*normalvariate(0, 1))
		if self.env.all_cost((self.x, self.y)) >= self.env.all_cost((x_, y_)):
			self.x = x_
			self.y = y_
			return True
		return False
