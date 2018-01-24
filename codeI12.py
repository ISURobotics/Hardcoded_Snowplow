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
I_track = [[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
plt.ion()
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0001)
#plt.imshow(I_track, cmap='gray', interpolation='none')

priority  = 'left' # can be preset before each event or on deciding the side to which the snow blade
# is directed
homing = priority
main_track = 1

#The setting up of the track based onpriority
if priority is 'left':
    avoidance    = 0
    return_route = 2
elif priority is 'right':
    avoidance    = 2
    return_route = 0

I_track[1][4] = 2
I_track[0][6] = 2
#I_track[1][6] = 2
#plt.imshow(I_track, cmap='gray', interpolation='none')
#time.sleep(5)
#######################################################################################################




print ("Waiting to receive messages...")

print ("The robot is initialized at point 1,0 on track I")
x=1
y=0
#I_track[x][y] = 1
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0001)
time.sleep(0.5)
#commands.move(x,y)
z = 0
while True:
    print (" The current position is ["+str(x) + "," + str(y)+"]")

    if I_track[avoidance][12] is 1:
        print("Avoidance control is being run")
        I_track[main_track][11]=3
        I_track[avoidance][12]=3

    elif I_track[main_track][12] is 2 and I_track[main_track][11] is 1:
        print("The last node is blocked")
        I_track[main_track][11] = 3

    elif I_track[main_track][11] is 0:
        if I_track[x][y+1] is 0:

            I_track[x][y] = 1
            y=y+1
            print("moving ahead")
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)
            #commands.move(x,y)


        elif I_track[x][y+1] is 2 :
            if y is 11:
                I_track[x][y]= 3
            I_track[x][y] = 1

            x = avoidance
            print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)

            if x is avoidance:
                z = 0
                for i in range(2):
                    z = z+1
                    I_track[x][y] = 3
                    if I_track[x][y+1] is 2:
                        print("An obstacle in the avoidance path")
                        print("returning back to main path")
                        for i in range(z-1):
                            print "moving to the position ["+str(x) + "," + str(y)+"]"
                            I_track[x][y] = 3
                            y = y-1
                            plt.imshow(I_track, cmap='gray', interpolation='none')
                            plt.pause(0.0005)
                            time.sleep(0.5)
                        I_track[x][y] = 3
                        plt.imshow(I_track, cmap='gray', interpolation='none')
                        plt.pause(0.0005)
                        time.sleep(0.5)
                        x = main_track
                        print "The current position is ["+str(x) + "," + str(y)+"]"
                        if priority is 'left':
                            avoidance  = 2
                        else:
                            avoidance  = 0

                    else:
                        y=y+1
                        print "moving to the position ["+str(x) + "," + str(y)+"]"
                        plt.imshow(I_track, cmap='gray', interpolation='none')
                        plt.pause(0.0005)
                        time.sleep(0.5)

                I_track[x][y] = 3
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0005)
                x = main_track
                print "The current position is ["+str(x) + "," + str(y)+"]"
                time.sleep(0.5)


    elif I_track[main_track][11] is 2:
        if I_track[x][y+1] is 0:

            I_track[x][y] = 1
            y=y+1
            print("moving ahead")
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)


        elif I_track[x][y+1] is 2:
            while y != 10:

                I_track[x][y] = 1
                print "false moving to the position ["+str(x) + "," + str(y)+"]"
                y = y+1
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0005)
                time.sleep(0.5)
            I_track[x][y] = 1
            x = avoidance
            print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)

            for i in range(2):
                I_track[x][y] = 3
                y=y+1
                print "moving to the position ["+str(x) + "," + str(y)+"]"
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0005)
                time.sleep(0.5)
            I_track[x][y] = 3
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            x = main_track
            print "The current position is ["+str(x) + "," + str(y)+"]"
            time.sleep(0.5)


    else:
        if I_track[return_route][0] is 1:
            x = main_track
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)
            print "final moving to the position ["+str(x) + "," + str(y)+"]"

            quit()

        else:
            print("Returning to home")
            I_track[x][y] = 1
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            time.sleep(0.5)
            x = return_route

            while y != 0:

                I_track[x][y] = 1
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0005)
                time.sleep(0.5)
                x= return_route
                print("Homing mode")
                if I_track[x][y-1] is 2:
                    I_track[x][y] = 1
                    x = main_track
                    print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
                    plt.imshow(I_track, cmap='gray', interpolation='none')
                    plt.pause(0.0001)
                    time.sleep(0.5)

                    if I_track[main_track][y] is 1 or 0:
                        for i in range(2):
                            I_track[x][y] = 3
                            y=y-1

                            print "avoid moving to the position ["+str(x) + "," + str(y)+"]"
                            plt.imshow(I_track, cmap='gray', interpolation='none')
                            plt.pause(0.0005)
                            time.sleep(.5)

                    else:
                        print("stuck")
                    I_track[x][y] = 3

                    x = return_route
                    I_track[x][y] = 1
                    print "The current position is ["+str(x) + "," + str(y)+"]"
                    time.sleep(0.5)
                    plt.imshow(I_track, cmap='gray', interpolation='none')
                    plt.pause(0.0005)
                    y=y-1
                    plt.imshow(I_track, cmap='gray', interpolation='none')
                    plt.pause(0.0005)

                    time.sleep(0.5)
                    print "The current position is ["+str(x) + "," + str(y)+"]"


                else:
                    I_track[x][y]=1
                    y=y-1
                    print "moving to the position ["+str(x) + "," + str(y)+"]"
