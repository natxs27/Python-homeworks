import random

def random_walk(start):
    for x in range(100):
        start = start + random.choice([-1,1])
    print(start)

random_walk(1)
