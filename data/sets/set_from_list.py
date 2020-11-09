def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation(include duplicates):")
    observation = input()
    observations.append(observation)
  return observations

def run():
  print("Counting observatinos...")
  observations = observed()
 # populate set
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

# display set
  for item in observations_set:
    observation = item [0]
    count = item [0]
    print(f"{observation} observed {count} times.")
run()