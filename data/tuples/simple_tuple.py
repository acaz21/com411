def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)


def run():
  min_l = likelihood()
  print(f"Minimum likelihood of falling: {likelihood()}%")


run()
