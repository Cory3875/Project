  import random

#intro statements
print 'Welcome to the game of math fun!'
print 'In this game, you will start on addition and end on division'
print 'If you get the answer right, you go onto the next stage, otherwise you start over'
print 

#variables
correctsofar = True
endgame = False
randint1 = random.randint(1,100)
randint2 = random.randint(1,99)
randint3 = random.randint(1,100)
randint4 = random.randint(1,99)
randint5 = random.randint(1,100)
randint6 = random.randint(1,99)
randint7 = random.randint(1,100)
randint8 = random.randint(1,99)
counter = 0
while (endgame == False):
    while (correctsofar == True):
        counter = 0
        #question 1
        print str(randint1) + " + " + str(randint2) + '=' + '?'
        rawinput1 = raw_input()
    
    
        if int(rawinput1) - randint2 == randint1:
            print 'You are correct, time to move onto the next level'
            counter = counter + 1
        if counter < 1:
            endgame = True
            
        print 
        print 'now you are on the subtraction level!'
        print 
    
        #question 2
        print str(randint3) + '-' + str(randint4) + '=' + '?'
        rawinput2 = raw_input()
    
        if int(rawinput2) + randint4 == randint3:
            print 'You are correct, time to move onto the next level'
            counter = counter + 2 
        print
        print 'now you are on the multiplication level!'
        print
    
        #question 3
        print str(randint5) + 'x' + str(randint6) + '=' + '?'
        rawinput3 = raw_input()
    
        if int(rawinput3) / randint6 == randint5:
            print 'You are correct, time to move onto the last level'
            counter = counter + 3
        print
        print 'now you are on the division level'
        print
    
        #question 4
        print str(randint7) + '/' + str(randint8) + '=' + '?'
        rawinput4 = raw_input()
    
        if int(rawinput4) * randint8 == randint7:
            counter = counter + 4
        print
        print 'You win!'  
        print
        print 'Do you wish to keep going?'
        rawinput5 = raw_input()
        if rawinput5 == 'yes':
            print
            print 'Time to start over'
            
        else:
            endgame = True
            correctsofar = False
            print 'Game Over'
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    