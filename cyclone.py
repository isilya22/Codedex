# Write code below

height=int(input ('Your Height in cm ?'))
credits=int(input ('How much credits do you have ?'))

if height >= 137 and credits >= 10 :
  print ("Enjoy the ride!")
elif height < 137 and credits >= 10 :
  print ("You are not tall enough to ride!")
elif height >= 137 and credits < 10 :
  print ("You don't have enough credits.")
else :
  print ("You don't meet the requirements.")