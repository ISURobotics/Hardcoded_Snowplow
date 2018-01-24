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
I_track = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
plt.ion()
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0001)
#plt.imshow(I_track, cmap='gray', interpolation='none')

priority  = 'right' # can be preset before each event or on deciding the side to which the snow blade is directed

# direction of movement
direction = 0 # plain declaration
# 1 means forward
# 2 means backward

main_track = 2
#####################################################################################################################
###########################THE AVOIDANCE AND ROUTE MODELLING#########################################################
#####################################################################################################################
#The setting up of the track based on priority
if priority is 'left':
    avoidance_I1    = 0
    avoidance_I2    = 1
    avoidance_I3    = 2
    avoidance_I4    = 3
    return_route    = 4
    ltrack = 1
    rtrack = 3
elif priority is 'right':
    avoidance_I1    = 4
    avoidance_I2    = 3
    avoidance_I3    = 2
    avoidance_I4    = 1
    return_route    = 0
    ltrack = 3
    rtrack = 1

#####################################################################################################################
I_track[1][2] = 2
I_track[3][9] = 2

print "The robot is initialized at point [2,0] on track I2"
x = 2
y = 0
I_track[x][y] = 1
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0005)
time.sleep(0.5)

def clean_snow_forward(X,y,direction,avoidance):
    x=X
    while True:
        print (" biggest error: The current position is ["+str(x) + "," + str(y)+"]")

        if I_track[x][10] is 1:
            y=y+1
            I_track[x][11] = 1
            print("moving ahead")
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)
            return

        elif I_track[x][10] is 0:
            if I_track[x][y+1] is 0:
                #checks whether it will detects any obstacle in front and goes onwards
                I_track[x][y] = 1
                y=y+1
                print("moving ahead")
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0001)
                time.sleep(0.5)
                #commands.move(x,y)
                #proceed to next iteration
            elif I_track[x][y+1] is 3:
                #checks whether it will detects any obstacle in front and goes onwards
                I_track[x][y] = 1
                y=y+1
                print("moving ahead")
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0001)
                time.sleep(0.5)
                #commands.move(x,y)
                #proceed to next iteration

            elif I_track[x][y+1] is 2 :
                if y is 10:
                    I_track[x][y]= 3
                I_track[x][y] = 1
                x = avoidance
                if I_track[x][11] is 2:
                    x = return_route
                else:
                    x = avoidance
                print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0001)
                time.sleep(0.5)

                #commands.move(x,y)
                #move to the mentioned direction ie. [avoidance,y]
                #move three blocks
                if x is avoidance:
                    z = 0
                    for i in range(2):
                        z = z+1
                        I_track[x][y] = 3
                        y=y+1
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
                            x = X
                            print "error 3:The current position is ["+str(x) + "," + str(y)+"]"


                        else:

                            print "moving to the position ["+str(x) + "," + str(y)+"]"
                            plt.imshow(I_track, cmap='gray', interpolation='none')
                            plt.pause(0.0005)
                            time.sleep(0.5)
                            #commands.move(x,y)
                            #run the movement algorithm here
                            #move two steps in the direction with same [avoidance, y = y+2]
                    I_track[x][y] = 3
                    plt.imshow(I_track, cmap='gray', interpolation='none')
                    plt.pause(0.0005)
                    x = X
                    print "The current position is ["+str(x) + "," + str(y)+"]"

                    time.sleep(0.5)
                    #commands.move(x,y)
                    # move back to the original track route
        #elif I_track[x][11] is 1:
            #I_track[x][y]=1
            #return
            #print "moving to the position ["+str(x) + "," + str(y)+"]"

        elif I_track[x][10] is 2:
            if I_track[x][y+1] is 0:
                #checks whether it will detects any obstacle in front and goes onwards
                I_track[x][y] = 1
                y=y+1
                print("moving ahead")
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0001)
                time.sleep(0.5)
                #commands.move(x,y)
                #proceed to next iteration

        elif I_track[x][y+1] is 2 :
            if y is 10:
                I_track[x][y]= 3
            I_track[x][y] = 1
            if I_track[1][11] is 2:
                x = X
            else:
                x = avoidance
            print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            time.sleep(0.5)
            #commands.move(x,y)
            #move to the mentioned direction ie. [avoidance,y]
            #move three blocks
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
                        x = X
                        print "error :The current position is ["+str(x) + "," + str(y)+"]"

                    else:
                        y=y+1
                        print "moving to the position ["+str(x) + "," + str(y)+"]"
                        plt.imshow(I_track, cmap='gray', interpolation='none')
                        plt.pause(0.0005)
                        time.sleep(0.5)
                            #commands.move(x,y)
                            #run the movement algorithm here
                            #move two steps in the direction with same [avoidance, y = y+2]
                I_track[x][y] = 3
                plt.imshow(I_track, cmap='gray', interpolation='none')
                plt.pause(0.0005)
                x = X
                print "or this? The current position is ["+str(x) + "," + str(y)+"]"
                time.sleep(0.5)
                #commands.move(x,y)
                # move back to the original track route

def clean_snow_backward(main_track,y,direction,avoidance):
    x=main_track
    I_track[x][y] = 1
    plt.imshow(I_track, cmap='gray', interpolation='none')
    plt.pause(0.0005)
    time.sleep(0.5)
    x = main_track
    #moving back to base along lower route
    while y != 0:
        # to return to base directly
        I_track[x][y] = 1
        print "The current position is ["+str(x) + "," + str(y)+"]"
        plt.imshow(I_track, cmap='gray', interpolation='none')
        plt.pause(0.0005)
        #time.sleep(0.5)
        x= main_track
        print("Homing mode")
        if I_track[x][y-1] is 2:
            I_track[x][y] = 1
            x = avoidance
            print "the new direction to achieve is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0001)
            #time.sleep(0.5)
            I_track[x][y] = 3
            #commands.move(x,y)
            #move to the mentioned direction ie. [avoidance,y]
            #move three blocks
            if I_track[main_track][y] is 1 or 0:
                for i in range(2):
                    plt.imshow(I_track, cmap='gray', interpolation='none')
                    plt.pause(0.0005)
                    time.sleep(0.5)
                    y=y-1
                    I_track[x][y] = 3
                    #time.sleep(0.5)
                    print "avoid moving to the position ["+str(x) + "," + str(y)+"]"
                    plt.imshow(I_track, cmap='gray', interpolation='none')
                    plt.pause(0.0005)
                    time.sleep(0.5)
                    #commands.move(x,y)
                    #run the movement algorithm here
                    #move two steps in the direction with same [avoidance, y = y+2]
            else:
                print("stuck")
            print "The current position is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            x = main_track
            I_track[x][y] = 1
            print "The current position is ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            y=y-1
            I_track[x][y] = 1
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            time.sleep(0.5)
            print("Homing")
            print "The current position is ["+str(x) + "," + str(y)+"]"


        else:
            I_track[x][y]=1
            #print "moving to the position ["+str(x) + "," + str(y)+"]"
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            time.sleep(0.5)
            y=y-1
            I_track[x][y]=1
            plt.imshow(I_track, cmap='gray', interpolation='none')
            plt.pause(0.0005)
            #print "1 moving to the position ["+str(x) + "," + str(y)+"]"
            #time.sleep(0.5)



print (" The current position is ["+str(x) + "," + str(y)+"]")
clean_snow_forward(main_track,0,1,avoidance_I2)
clean_snow_backward(rtrack,11,0,return_route)
clean_snow_forward(ltrack,0,1,avoidance_I1)
clean_snow_backward(return_route,11,0,return_route)
print("Returning to home")
x = main_track
I_track[x][y] = 1
print ("The current position is ["+str(x) + "," + str(y)+"]")
plt.imshow(I_track, cmap='gray', interpolation='none')
plt.pause(0.0005)
time.sleep(0.5)



#I_track[1][6] = 2
#plt.imshow(I_track, cmap='gray', interpolation='none')
#time.sleep(5)
#######################################################################################################
