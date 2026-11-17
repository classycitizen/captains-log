from dateline import date

year = int(input("Birth year? "))
month = int(input("Birth month(1-12)? "))
day = int(input("Birth day "))

today = date.today()
age = today.year - year

if (today.month, today.day) < (month, day):
  age -= 1

print("You are", age, "years old.")
