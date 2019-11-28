from random import normalvariate


class Bee:
	def __init__(self, x, y, env):
		self.x = x
		self.y = y
		self.env = env
		self.cost = 999999999999999

	def one_plus_one(self, omega, omega_min, c1=0.82, c2=1.2, m=10, max_iter=1000):
		fi = 0
		k = 0
		while omega >= omega_min and k < max_iter:
			x_, y_ = (self.x + (omega * normalvariate(0, 1)), self.y + (omega * normalvariate(0, 1)))
			if self.env.all_cost((self.x, self.y)) >= self.env.all_cost((x_, y_)):
				self.x = x_
				self.y = y_
				fi += 1
			if k % m == 0:
				if fi < 0.2:
					omega *= c1
				elif fi > 0.2:
					omega *= c2
			if fi % m == 0:
				fi = 0
			k += 1


