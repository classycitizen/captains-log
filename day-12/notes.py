note = input("Write a note: ")

with open("notes.txt", "a") as  file:
  file.write(note + "\n")

print("Saved! Your notes so far:")

with open("notes.txt", "r") as file:
  print(file.read())
