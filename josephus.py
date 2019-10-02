# Get the number of soldiers
num = int(input("Enter number of soldiers: "))
army = []
temp = []

# Populate the army
for i in range(0,num):
  army.append(i + 1)

# Print them before they are dead
print("Army: ", army)

# Start killing
while len(army) > 1:
  # Check if number of soldiers is even
  if len(army) % 2 != 0:
    for i in range(1, len(army)):
      if i % 2 == 0:
        temp.append(army[i])
  else:
    for i in range(0, len(army)):
      if i % 2 == 0:
        temp.append(army[i])

  # Reset for next iteration
  army = temp
  temp = []

  # Print the remaining soldiers
  print(army)

# Print the survivor
print("Survivor:", army)
