from environment import Environment

env1 = Environment()
env1.get_input()
env1.set_field()
env1.add_bees(1000)
env1.algo11(omega=1, omega_min=0.5)
print("The factory needs to be built at coordinates:" + str(env1.best_bee))




