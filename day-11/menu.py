menu = {
  "turkey": 15,
  "pie": 6,
  "stuffing": 4,
  "rolls": 2

}

while True:
  food = input("What do you want? (or quit) ")

  if food == "quit":
    break

  if food in menu:
    print(food, "costs $" + str(menu[food]))

  else:
    print("Sorry, we dont have", food)
