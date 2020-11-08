print("Please enter a seaquence")
seaquence = input()
print ("Please enter the character for the marker")
marker = input()

counting = False
count = 0

for character in seaquence:
  if (character == marker and counting == True):
    print("found last marker")
  elif (character == marker and counting == False):
    print("found first marker")
    counting = True
  elif (character != marker and counting == True):
    count += 1
print("The distance is {}." .format(count))






















