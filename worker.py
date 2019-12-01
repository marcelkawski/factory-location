from random import normalvariate


class Bee:
	def __init__(self, x, y, env):
		self.x = x
		self.y = y
		self.env = env
		self.cost = self.env.all_cost((x, y))
		self.k = 0

	def one_plus_one(self, omega, omega_min, c1=0.81, c2=1.2, m=10, max_iter=1000):
		fi = 0
		k = 0
		while omega >= omega_min and k < max_iter:
			x_, y_ = (self.x + (omega * normalvariate(0, 1)), self.y + (omega * normalvariate(0, 1)))
			if self.env.all_cost((self.x, self.y)) >= self.env.all_cost((x_, y_)):
				self.x = x_
				self.y = y_
				fi += 1
			if k % m == 0:
				fi = fi/m
				if fi < 0.2:
					omega *= c1
				elif fi > 0.2:
					omega *= c2
				fi = 0
			k += 1
		self.cost = self.env.all_cost((self.x, self.y))
		self.k = k

	def __str__(self):
		return f"x: {self.x} y: {self.y} cost: {self.cost} steps: {self.k}"
