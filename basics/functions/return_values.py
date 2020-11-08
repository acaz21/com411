def sum_weights(bop_weight, beep_weight):
  total = bop_weight + beep_weight
  return total

def calc_avg_weight(bop_weight, beep_weight):
  avg_weight = (beep_weight + bop_weight) / 2
  return avg_weight

def run():
  print("Weight Bop:")
  bop_weight = float(input())
  print("Weight Beep:")
  beep_weight = float(input())

  print("Calcualte sum or average weights?")
  choice = input()

  if (choice == "sum"):
    print("The total weight is", sum_weights(beep_weight, bop_weight))
  elif(choice == "average"):
    print("The average weight is", calc_avg_weight(beep_weight, bop_weight))
  else:
    print("Error, unexpected input, check spelling")

run()