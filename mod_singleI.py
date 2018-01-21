import commands
import os
#from socket import *
#import socket
#import serial
import time
from time import sleep
#import matplotlib
import math
from math import sqrt
from math import cos
from math import sin
import sys
import matplotlib.pyplot as plt


#declaring the matrix list for the buffer only one required. x= 0,1,2 ; y= 0,1,.....,8,9,10 (including the extra space for turning)
############0,1,2,3,4,5,6,7,8,9,10,#0,1,2,3,4,5,6,7,8,9,10,#0,1,2,3,4,5,6,7,8,9,10###############
import matplotlib.pyplot as plt
I_track = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
plt.ion()
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0001)
#plt.imshow(I_track, cmap='gray', interpolation='none')

priority  = 'left' # can be preset before each event or on deciding the side to which the snow blade
# is directed

main_track = 1

#The setting up of the track based onpriority
if priority is 'left':
    avoidance    = 0
    return_route = 2
elif priority is 'right':
    avoidance    = 2
    return_route = 0
I_track[1][4] = 2
#I_track[1][6] = 2
#plt.imshow(I_track, cmap='gray', interpolation='none')
#time.sleep(5)
#######################################################################################################




print "Waiting to receive messages..."

print "The robot is initialized at point 1,0 on track I"
x=1
y=0
#I_track[x][y] = 1
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0001)
time.sleep(2)
#commands.move(x,y)

while True:
    print " The current position is ["+str(x) + "," + str(y)+"]"

    #if #objectdected:
    #    I_track[x][y+1] = '2'
        # This allows us to notify the buffer that on the list there is an object
    #Check if the sensor is detecting any obstacle and
    if I_track[1][10] is 0:
        if I_track[x][y+1] is 0:
            #checks whether it will detects any obstacle in front and goes onwards
            I_track[x][y] = 1
            y=y+1
            print("moving ahead")
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(2)
            #commands.move(x,y)
            #proceed to next iteration

        elif I_track[x][y+1] is 2:
            I_track[x][y] = 1
            x = avoidance
            print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(2)
            #commands.move(x,y)
            #move to the mentioned direction ie. [avoidance,y]
            #move three blocks
            for i in range(2):
                I_track[x][y] = 1
                y=y+1
                print "moving to the position ["+str(x) + "," + str(y)+"]"
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0005)
                time.sleep(2)
                #commands.move(x,y)
                #run the movement algorithm here
                #move two steps in the direction with same [avoidance, y = y+2]
            I_track[x][y] = 1
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            x = main_track
            print "The current position is []"+str(x) + "," + str(y)+"]"
            time.sleep(2)
            #commands.move(x,y)
            # move back to the original track route

    else:
        print("Returning to home")
        I_track[x][y] = 1
        plt.imshow(I_track, cmap='gray', interpolation='none')
        plt.pause(0.0005)
        time.sleep(2)
        x = return_route
        #moving back to base along lower route
        while y != 0:
            # to return to base directly
            I_track[x][y] = 1
            print "moving to the position ["+str(x) + "," + str(y)+"]"
            y = y-1
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            time.sleep(2)
            #commands.move(x,y)
            #move them one step

    if I_track[return_route][0] is 1:
        x = main_track
        plt.imshow(I_track, cmap='gray', interpolation='none')
        plt.pause(0.0001)
        time.sleep(2)
        print "moving to the position ["+str(x) + "," + str(y)+"]"
        #sys.exit()
        quit()
        #commands.move(x,y)
        #moving to orgin position

#UDPSock.close()
