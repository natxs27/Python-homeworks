import random
import itertools

iter_binary = itertools.cycle([0,1])
# for i in iter_binary:
#     print(i)

class CoinToss:

    def __init__(self,sequence):
        self.data = sequence

    def iter_random(sequence):
        while True:
            yield random.choice(sequence)

iter_coin = CoinToss.iter_random([0,1])
# for i in iter_coin:
#     print(i)


iter_BackForth = itertools.cycle([0,1,0,-1])
#for i in iter_BackForth:
#    print(i)

print(next(iter_binary), end =" ")
print(next(iter_binary), end =" ")
print(next(iter_binary), end =" ")
print(next(iter_binary), end =" ")
print(next(iter_binary))

print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin), end =" ")
print(next(iter_coin))

print(next(iter_BackForth), end =" ")
print(next(iter_BackForth), end =" ")
print(next(iter_BackForth), end =" ")
print(next(iter_BackForth), end =" ")
print(next(iter_BackForth), end =" ")
print(next(iter_BackForth), end =" ")
print(next(iter_BackForth), end =" ")
print(next(iter_BackForth))
