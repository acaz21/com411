# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...\nThe phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")
  





















