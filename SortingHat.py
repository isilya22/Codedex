# Write code below 💖
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

answerQa=int(input('Q1 : Do you like Dawn (1) or Dusk (2)?'))
if answerQa==1:
  Gryffindor +=1
  Ravenclaw +=1
elif answerQa==2: 
  Hufflepuff +=1
  Slytherin +=1
else :
  print ('wrong input')

answerQb=int(input('Q2 : When I’m dead, I want people to remember me as: The Good (1), The Great (2), The Wise (3) or The Bold (4)'))
if answerQb==1:
  Hufflepuff +=2
elif answerQb==2:
  Slytherin +=2
elif answerQb==3:
  Ravenclaw +=2
elif answerQb==4:
  Gryffindor +=2
else :
  print ('wrong input')

answerQc=int(input('Q3 : Which kind of instrument most pleases your ear? The violin (1), the trumpet (2), the piano (3) or the drum (4)'))
if answerQc==2:
  Hufflepuff +=4
elif answerQc==1:
  Slytherin +=4
elif answerQc==3:
  Ravenclaw +=4
elif answerQc==4:
  Gryffindor +=4
else :
  print ('wrong input')

if Gryffindor > Slytherin and Gryffindor > Ravenclaw and Gryffindor > Hufflepuff:
  print ('Congrats ! You are in Gryffindor')
if Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
  print ('Congrats ! You are in Slytherin')
if Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
  print ('Congrats ! You are in Ravenclaw')
if Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
  print ('Congrats ! You are in Hufflepuff')

print ('Gryffindor', Gryffindor)
print ('Slytherin', Slytherin)
print ('Ravenclaw', Ravenclaw)
print ('Hufflepuff', Hufflepuff)

