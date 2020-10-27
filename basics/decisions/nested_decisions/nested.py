print("What type of cover does this book have?")
book_cover = input()

if (book_cover == "soft"):
  print("Is the book perfect-bound?")
  answer = input()
  if (answer == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stiches are great for short books.")

else:
  print("Books with hard covers can be more expensive!")

























