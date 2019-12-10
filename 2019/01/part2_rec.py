def calculateFuel(mass):
  if mass <= 0: return 0
  fuel = int(int(mass) / 3) - 2
  return (0, fuel + calculateFuel(fuel))[bool(fuel > 0)]

sum = 0
line = 0
file = open("input.txt", "r")
for mass in file:
  print("line: " + str(line) + ", mass: " + mass, end='')
  line += 1
  sum += calculateFuel(int(mass))
file.close()
print("\n\nthe sum is: " + str(sum))
