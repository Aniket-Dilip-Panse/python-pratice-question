import random
print(random.random())
print(random.randint(1,11))
print(random.uniform(0.1, 1.0))
list = [1,2,4,3,2,4,14,44,414,4,42,444414,4,14,252525,255,25,5252,52,2,2252,52,66]
print(f'original list = {list}')
random.shuffle(list)
print(f'list after shuffle {list}')
print(random.choice(list))
print(random.betavariate(10.0, 15.0))
print(random.choices(list))
print(random.getstate())
print(random.getrandbits(64))
print(random.triangular(2,3,4))