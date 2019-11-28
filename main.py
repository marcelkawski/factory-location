from environment import Environment

env1 = Environment()
env1.get_input()
env1.set_field()
env1.add_bees(2)
gb_x, gb_y = env1.workers[0].x, env1.workers[0].y
gb_cost = env1.workers[0].cost
for bee in env1.workers:
    bee.one_plus_one(1, 0.5)
    bee.cost = bee.env.all_cost((bee.x, bee.y))
    if bee.cost < gb_cost:
        gb_cost = bee.cost
        gb_x = bee.x
        gb_y = bee.y
    print(bee.cost, bee.x, bee.y)
print("The factory needs to be built at coordinates: (%f, %f)." % (gb_x, gb_y))






