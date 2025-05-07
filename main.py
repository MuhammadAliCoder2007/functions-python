#Muhammad Ali
#30 Novemeber 2023
# 1
# calculates the number of factors
# def numFactors(num):    #defining the function
#   count  =  0   #initializing count, which counts factors
#   for i in range(1,num+1):  #the number check from 1, to the num+1, cuz the number itself counts as a factor
#     if num%i ==  0: #if num // i don't have a remainder, it counts as a factor
#       count+=1  #counts all the factors
#   return count  #returns it

# 2
# prints the word from the first list that are not in the second list
# def subtract(list1,list2):  #defing function, list1 and 2 and are parameters
#   list3 = []    #list in which all the numbers in list 1 that are not list2 goes into it
#   for i in range(len(list1)):   #running the loop till the length of list1
#     if list1[i] not in list2:   #id number in list 1 that is not in list 2, it appends it to list3
#       list3.append(list1[i])
#
#   return list3  #returns the list


# 3
#justifies the word
# def justify(words,size):    #defing the function
#     tot_char = len("".join(words))  #counts the total characters
#     spaces = size - tot_char    #calculates total number of spaces
#     space_bw_words = spaces//(len(words)-1) #calculates spaces between every word
#
#     if space_bw_words <=0:  #when spaces are not enough to be distribiuted, spaces bw words is less than -
#         return " ".join(words)  #returns all the words with one space
#     elif spaces%(len(words)-1)==0:  #when spaces distribute evenly
#         return (space_bw_words*(" ")).join(words)   #return the word, with that number od spaces
#     else:   #when spaces dont divide evenly
#         result1 =  (space_bw_words*(" ")).join(words[:-1])  #first it adds spaces bw words except the last word
#         remainder = spaces%(len(words)-1)   #calculating the remainder spaces
#         space_bw_words+=remainder   #adding it to the spaces words
#         result2 = " "*space_bw_words+(words[-1])    #putting that much space and then
#         return result1+result2  #reuturn the sentence with all the words and spaces

# 4
#draws a grid on the screen
# from pygame import *
# screen = display.set_mode((800,600))
#
# RED = (255, 0, 0)    # ALL CAPS is used for constants
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# WHITE = (255,255,255)
# def grid(x,y,w,h):  #defing function taking coordinates and size(width and height)
#     if w >10 and h>10:  #base case
#
#         rect= [(x,y),(w,h)] #list of points for rect
#         draw.rect(screen,WHITE,rect,1)
#         #draws rect in four different places and divides the size by 2 to make the grid
#         grid(x,y,w/2,h/2)
#         grid(x,y+h/2,w/2,h/2)
#         grid(x+w/2,y,w/2,h/2)
#         grid(x+w/2,y+h/2,w/2,h/2)
#
# grid(100,50,512,512)
# running = True
# while running:
#     for evt in event.get():
#         if evt.type == QUIT:
#             running = False
#
#     mx, my = mouse.get_pos()
#     mb = mouse.get_pressed()
#     # ----------------------------------
#
#
#     # ----------------------------------
#     display.flip()
#
# quit()

# 5
#lightning that draws a lightning on the screen
# from pygame import *
# from math import *
# from random import *
#
# screen = display.set_mode((800,600))
#
# RED = (255, 0, 0)    # ALL CAPS is used for constants
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
#
# def xy(x,y):
#     size = randint(100,150) #random angles and sizes for lightning to come down
#     ang = randint(225,315)
#     #convering randians to degrees
#     x2 = x + cos(radians(ang))*size
#     y2 = y - sin(radians(ang))*size
#     return x2,y2
#
# def lightning(x,y, counter =0): #takes coordinates for lightning and counter is for to stop some of the lightning before the screen ends
#     if y<600 and counter<6:
#         x2,y2 = xy(x,y) #connecting x,y and x2,y2 with that size and angle
#
#         draw.line(screen,(255,255,0),(x,y),(x2,y2),2)   #draws bolt
#     #draws lightning
#         lightning(x2,y2, counter+1)
#         lightning(x2,y2, counter+2)
#         lightning(x2,y2, counter+3)
#
#
#
# lightning(400,10)
#
#
# running = True
# while running:
#     for evt in event.get():
#         if evt.type == QUIT:
#             running = False
#
#     screen.fill(0)
#     time.wait(1000)
#     lightning(400,10)
#
#
#     mx, my = mouse.get_pos()
#     mb = mouse.get_pressed()
#     # ----------------------------------
#
#     # ----------------------------------
#     display.flip()
#
# quit()


# 6
#starthat draws a 5-pointed star on the screen
# from pygame import *
# from math import *
# from random import *
#
# screen = display.set_mode((800,600))
#
# RED = (255, 0, 0)    # ALL CAPS is used for constants
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
#
# def xy1(x, y, size, ang):
#   x2 = x + cos(radians(ang))*size
#   y2 = y + sin(radians(ang))*size
#   return (x2, y2)
#
# #this is thing that I got from my dad, and I more than somewhat, and I will spend more time to understand it too
# def getangle(i):
#     if i == 0:  #start point
#         return 0
#     elif i == 1:    #endpoint
#         return 360-72
#     elif i == 2:
#         return 72
#     elif i == 3:
#         return 0
#     elif i == 4:
#         return 180-36
#     elif i == 5:
#         return 72
#     elif i == 6:
#         return 180+36
#     elif i == 7:
#         return 180-36
#     elif i == 8:
#         return 360-72
#     elif i == 9:
#         return 180+36
#
#
# def star(x, y, size,col):
#     start = (x, y)
#     for i in range(10): #within range of that 10 angles
#         (x1, y1) = start    #start postion
#         angle = getangle(i) #gets the angle
#         end_pos = xy1(x1, y1, size, angle)  #connected to first position
#         draw.line(screen, col, start, end_pos)
#         start = end_pos #start position swtiches to end position
# star(200,200,200,(255,245,24))
#
#
# running = True
# while running:
#     for evt in event.get():
#         if evt.type == QUIT:
#             running = False
#
#     mx, my = mouse.get_pos()
#     mb = mouse.get_pressed()
#     # ----------------------------------
#
#     # ----------------------------------
#     display.flip()
#
# quit()


# 7
#draws an analog clock in the middle of the screen
# from pygame import *
# from math import *
# from random import *
#
# import datetime
#
#
# def xy(x, y, size, ang):
#     x2 = x + cos(radians(ang)) * size
#     y2 = y - sin(radians(ang)) * size
#     return x2, y2
#
#
# def getHourAngle(hour): #calculates the hour
#     angle = 0
#     if hour > 3:    #when the hour is greater than 3 you have subtract by 360, to get the angle
#         angle = 360
#     return angle + 90 - (hour * 30)
#
#
# def getMinuteOrSecondAngle(duration):   #calculates the min and secs
#     angle = 0
#     if duration > 15:
#         angle = 360
#     return angle + 90 - (duration * 6)
#
#
# def clock(hour, minute, second):
#     print(hour, minute, second)
#     size = 200
#
#     draw.circle(screen, (255, 255, 255), (500, 375), 200, 1)
#     draw.line(screen, (0, 255, 255), (500, 375), (xy(500, 375, size - 100, getHourAngle(hour))), 10)    #draws the line for hour
#     draw.line(screen, (255, 0, 255), (500, 375), (xy(500, 375, size - 50, getMinuteOrSecondAngle(minute))), 5)  #draws the line for minute
#     draw.line(screen, (255, 255, 0), (500, 375), (xy(500, 375, size - 25, getMinuteOrSecondAngle(second))), 1)  #draws the line for seconds
#
#     for a in range(0,360,30):
#         draw.circle(screen,(255,255,255),(xy(500,375,190,a)),5) #ticks around the clock
#
# screen = display.set_mode((1000, 750))
#
# running = True
# while running:
#     for e in event.get():
#         if e.type == QUIT:
#             running = False
#
#     screen.fill(0)
#     now = datetime.datetime.now()
#     clock((now.hour - 1) % 12 + 1, now.minute, now.second)
#     display.flip()
#     time.wait(20)
#
# quit()
