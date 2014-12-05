import random
print 'Welcome to the game of math fun!'
print 'In this game, you will start on addition and end on division'
print 'If you get the answer right, you go onto the next stage, otherwise you start over'
print 

randint1 = random.randint(1,100)
randint2 = random.randint(1,99)

print str(randint1) + " + " + str(randint2) + '=' + '?'
rawinput1 = raw_input()
while int(rawinput1) - randint2 == randint1 == True:
    print 'You are correct, time to move onto the next level' 

if int(rawinput1) - randint2 == randint1:
    print 'You are correct, time to move onto the next level'
else: 'You are wrong, now you have to start over'

print 
print 'now you are on the subtraction level!'
print 

randint3 = random.randint(1,100)
randint4 = random.randint(1,99)
print str(randint3) + '-' + str(randint4) + '=' + '?'
rawinput2 = raw_input()

if int(rawinput2) + randint4 == randint3:
    print 'You are correct, time to move onto the next level'