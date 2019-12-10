def calculateFuel(mass):
  if mass > 0:
    fuel = int(int(mass) / 3) - 2
    if fuel > 0:
      return fuel
    else:
      return 0

sum = 0
line = 0
f = open("input.txt", "r")
for x in f:
  print("line: " + str(line) + ", mass: " + x)
  line += 1
  y = int(x)
  while y > 0:
    print(y)
    fuel = calculateFuel(y)
    if fuel == 0: break
    sum += fuel
    y = fuel
f.close()
print("the sum is: " + str(sum))
