print ("What level of brightnessis required?")
brightness_required = int(input())

print("Adjusting brightness...")
print()

for brightness in range(2, brightness_required + 1 , 2):
  print("Beep's brightness level:", "*" * brightness)
  print("Bop's brightness level:", "*" * brightness)
    
print("Adjustments complete!")
























