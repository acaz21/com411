def dispaly_ladder(steps):
  for step in range(0, steps, 1):
    print("| | \n***")
  print("| |")  
3
def create_ladder():
  print("How many steps?")
  steps = int(input())
  dispaly_ladder(steps)

create_ladder()