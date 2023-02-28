import turtle
import random
import sys


painter = turtle.Turtle()
painter.hideturtle()
color1 = "black"
painter.speed(1)
painter.color(color1)
painter.shape("classic")
space = 50  # the radius of the circle
angle = 65  # experiment
seg = int(360 / angle)  # the length of a line




answer = input("do you want to play hangman? (yes, no)")
if (answer == "yes"):
   print("splendid!")
   painter.speed(3)
   painter.hideturtle()
   painter.pensize(8)
 # code to create the stand
   painter.begin_fill()
   painter.forward(150)
   painter.end_fill()
   painter.forward(-70)
   painter.left(90)
   painter.forward(175)
   painter.left(90)
   painter.forward(60)
   painter.left(90)
   painter.pensize(2)
   painter.forward(30)
   painter.penup()
   painter.pensize(5)
   painter.goto(40,0)
   painter.pendown()
   painter.left(135)
   painter.forward(53)
   painter.penup()
   painter.goto(120,0)
   painter.left(90)
   painter.pendown()
   painter.forward(55)
   painter.penup()
   painter.goto(80,145)
   painter.pendown()
   painter.forward(45)
   headwrite = painter.pos()


# code for the head
   def headdraw():
       painter.penup()
       painter.goto(20,145)
       painter.left(45)
       painter.pensize(3)
       painter.pendown()
       painter.setheading(180)
       painter.circle(15)
       painter.circle(15,180)




# code for the body
   def bodydraw():
       painter.right(90)
       painter.forward(45)




# code for the left arm
   def leftarmdraw():
       painter.forward(-30)
       painter.left(120)
       painter.forward(30)
 
# code for the right arm
   def rightarmdraw():
       painter.forward(-30)
       painter.right(240)
       painter.forward(30)
       painter.forward(-30)
       painter.left(120)
       painter.forward(30)




# code for the right leg
   def rightlegdraw():
       painter.right(30)
       painter.forward(35)
       painter.penup()
       painter.forward(-35)




# code for the left leg
   def leftlegdraw():
       painter.left(60)
       painter.pendown()
       painter.forward(35)




# code for the eyes and face
   def facialfeaturesdraw():
       painter.penup()
       painter.speed(100)
       painter.goto(13,132)
       painter.pendown()
       painter.circle(1)
       painter.penup()
       painter.goto(25,132)
       painter.pendown()
       painter.circle(1)
       painter.penup()
       painter.goto(25,120)
       painter.pendown()
       painter.right(195)
       painter.circle(5,150)






   def endscreendraw():
       painter.hideturtle()
       painter.speed(100)
       painter.pensize(3)
       painter.pendown()
       painter.pensize(3)
       painter.circle(15)
       painter.circle(15,180)  
       painter.right(90)
       painter.forward(45)
       painter.forward(-30)
       painter.left(120)
       painter.forward(30)
       painter.forward(-30)
       painter.right(240)
       painter.forward(30)
       painter.forward(-30)
       painter.left(120)
       painter.forward(30)
       painter.right(30)
       painter.forward(35)
       painter.penup()
       painter.forward(-35)
       painter.left(60)
       painter.pendown()
       painter.forward(35)
       painter.penup()
       painter.goto(-5,13)
       painter.pendown()
       painter.circle(1)
       painter.penup()
       painter.goto(6,13)
       painter.pendown()
       painter.circle(1)
       painter.penup()
       painter.goto(-5,23)
       painter.pendown()
       painter.right(195)
       painter.circle(5,150)
       painter.penup()
       painter.goto(-700,-80)
       painter.fillcolor("orange")
       painter.begin_fill()
       painter.pencolor("red")
       painter.pendown()
       painter.left(285)
       painter.forward(1400)
       painter.right(90)
       painter.forward(500)
       painter.right(90)
       painter.forward(1400)
       painter.right(90)
       painter.forward(500)
       painter.end_fill()


# code for the alternative answer



words = ["spacer", "blanket","string","rainfall","laptop","america","baseball","shape","coupon","exfoliate","xanex","adequate","liquid","exact","bandana","hairline","nutrition","neutrino","jolly","reserve","splendid","turtle","zebra","wealth","frontier","doctrine","perplex","invisible","question","piano","house","hallway","pneumonoultramicroscopicsilicovolcanoconiosis"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" , "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
trtl = turtle.Turtle()
wordbankx = 220
wordbanky = -200
wordbank = []
#makes counter of how many mistakes
counter = 0
trtl.penup()
trtl.goto(260,200)
trtl.pendown()
trtl.write(counter)




#choose which word to guess and add the spaces
chsn = random.choice(words)
chsnletters = len(chsn)
xpos = -250
ypos = -60
for blank in range(chsnletters):
   spcebv = []
   trtl.penup()
   trtl.goto (xpos, ypos)
   trtl.pendown()
   trtl.forward(45)
   spcebv.append(painter.xcor) 
   xpos+= 60
#turn word into an array of its letters






chsnarray=list()
chsnarray.extend(chsn)


#assign letters to spaces
trtl.speed(200)
xpos = -230
ypos = -55
trtl.penup()




#prompt user to guess a letter or word
while (counter < 6):
   choice = input("guess a letter or a word")
   if (choice == "word"): #if choose word
       gss = input("guess your word")
       if (gss == chsn): #if guess correct
           print(chsn, "was correct! you win!")
           sys.exit() 
       else :
            print(gss, "is not correct.") #if guess incorrect
            counter += 1  
            trtl.goto(260,210)
            trtl.shape("square")
            trtl.fillcolor("white")
            trtl.stamp()
            trtl.penup()
            trtl.goto(260,203)
            trtl.pendown()
            trtl.write(counter)
       if (counter == 1):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
       elif (counter == 2):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
       elif  (counter == 3):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
       elif (counter == 4):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
           rightarmdraw()
       elif  (counter == 5):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
           rightarmdraw()
           rightlegdraw()
       elif  (counter == 6):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
           rightarmdraw()
           rightlegdraw()
           leftlegdraw()
           print("you lost.")
           endscreendraw()
           print("The word was", chsn, ".")
           sys.exit()


  
   elif (choice == "letter"): #if choose letter
        gss = input("guess your letter")
       
        if (chsnarray.count(gss) > 0):
            print("this letter is in the chosen word.")
            trtl.penup()
            if (chsnarray.count(gss) > 1):
               for index, character in enumerate(chsnarray):
                   if (character == gss):
                       xposition = index
                       trtl.penup()
                       trtl.goto(xposition*60-230,-60)
                       trtl.pendown()
                       trtl.write(gss)
                       trtl.penup()
               trtl.penup()
               trtl.goto(wordbankx, wordbanky)
               trtl.pendown()
               trtl.write(gss)
               trtl.penup()
               trtl.hideturtle()
               wordbankx = wordbankx + 15
               wordbank.append(gss)
              
            else :
               xposition = chsnarray.index(gss)
               trtl.penup()
               trtl.goto(xposition*60-230,-60)
               trtl.pendown()
               trtl.write(gss)
               trtl.penup()
               trtl.goto(wordbankx, wordbanky)
               trtl.pendown()
               trtl.write(gss)
               trtl.penup()
               trtl.hideturtle()
               wordbankx = wordbankx + 15
               wordbank.append(gss)
      
            xposition = chsnarray.index(gss)
            xposition*60 - 220


        else:
           counter = counter + 1
           trtl.goto(260,210)
           trtl.shape("square")
           trtl.fillcolor("white")
           trtl.stamp()
           trtl.penup()
           trtl.goto(260,203)
           trtl.pendown()
           trtl.write(counter)
           print("this letter is not in the chosen word.")
           trtl.penup()
           trtl.goto(wordbankx, wordbanky)
           trtl.pendown()
           trtl.write(gss)
           trtl.penup()
           trtl.hideturtle()
           wordbankx = wordbankx + 15
           wordbank.append(gss)
       
        if (counter == 1):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
        elif (counter == 2):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
        elif  (counter == 3):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
        elif (counter == 4):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
           rightarmdraw()
        elif  (counter == 5):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
           rightarmdraw()
           rightlegdraw()
        elif  (counter == 6):
           trtl.goto(headwrite)
           trtl.setheading(270)
           headdraw()
           bodydraw()
           leftarmdraw()
           rightarmdraw()
           rightlegdraw()
           leftlegdraw()
           print("you lost.")
           endscreendraw()
           print("The word was", chsn, ".")
           sys.exit()
  
     




wn = trtl.Screen()
wn.mainloop()



