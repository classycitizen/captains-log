import random

roll = 0
tries = 0

while roll != 6:
  roll = random.randint(1, 6)
  tries += 1
  print("rolled a", roll)

print("Got a 6 in", tries, "tries!")
