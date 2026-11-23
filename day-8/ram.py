ram = [0] * 16

while True:
  command = input("read, write, show or quit? ")

  if command == "write":
    address = int(input("Address (0-15): "))
    value = int(input("Value (0-255): "))
    ram[address] = value % 256
  elif command == "read":
    address = int(input("Address (0-15): "))
    print("Address", address, "holds", ram[address])
  elif command == "show":
    print(ram)
  elif command == "quit":
    break
  
