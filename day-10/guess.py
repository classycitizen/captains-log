import random

def hint(guess, secret):
  if guess < secret:
      return "Too low!"
  else:
      return "Too high!"

secret = random.randint(1, 20)
guess = 0
tries = 0

while guess != secret:
  guess = int(input("Guess a number from 1 to 20: "))
  tries += 1
  if guess != secret:
    print(hint(guess, secret))

print("You got it in", tries, "tries!")
