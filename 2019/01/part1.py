sum = 0
f = open("input.txt", "r")
for x in f:
  # print(x)
  sum += int(int(x) / 3) - 2
f.close()
print("the sum is: " + str(sum))
