def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction")
  dir = directions()
  for index in range(len(dir)):
    print("{}: {}". format(index, dir[index]))
  index = int(input())
  return dir[index]
  
def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    route.append(menu())
  print(f"Escape route: {route}")

run()