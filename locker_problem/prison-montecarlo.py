#!/usr/bin/env python3

"""
THE LOCKER PUZZLE
- The warden of a prison with 100 prisoners decides to play a game with them.
- Each prisoner is numbered 1 to 100.
- He puts 100 boxes in a room, also numbered 1 to 100.
- Each prisoner's number is in one of the boxes
- The numbers in the boxes are randomized.
- All the prisoners can go free if given 50 chances, they find the box with
  their number.

Premise - strategy with highest chance of success is they pick the box with
their own number, then then follow the number they get to the next box.
eventually, it must loop around to their number. If no loop is under 50 chances,
they will all go free.
Probability they all go free is then the chance that there is no loop, >50 numbers.
"""

import random
import time

boxes=[]
prisonercount=100

def setupboxes():
    global prisonercount
    initarray=[]
    finalarray=[]
    for a in range(prisonercount):
        initarray.append(a)
    while len(initarray)>0:
        pick=int(random.random()*len(initarray))
        finalarray.append(initarray.pop(pick))
    return finalarray
        
def prisonerpickownbox(pnum, chances):
    """
    takes prisoner's number and number of chances
    """
    global boxes
    checks=0
    checkbox=pnum
    while checks<chances:
        checks+=1
        checkbox=boxes[checkbox]
        if checkbox==pnum:
            return True
    return False

def checkallprisoners():
    """
    True if all prisoners find their number
    If any fail, returns false.
    """
    global prisonercount
    for pnum in range(prisonercount):
        if not prisonerpickownbox(pnum,prisonercount/2):
            return False
    return True
        

if __name__=="__main__":
    wins=0.0
    loss=0.0
    iterations=0
    
    time_start=time.time()
    showresulttime=1
    lastcount=0
    while True:                     #constant loop
        iterations+=1               #increment iter counter
        boxes=setupboxes()          #init boxes
        if checkallprisoners():     #check all prisoners
            wins+=1                 #keep tally of successes
        else:
            loss+=1        

        time_now=time.time()
        if time_now-time_start>showresulttime: #output every second
            result=float(wins)/float(wins+loss)
            rate=int(iterations/(time_now-time_start))
            lastcount=iterations
            print("{} iterations of {} prisoners... {} rate:{}/s".format(
                str(iterations).rjust(8),prisonercount,str(result).ljust(20),rate)
            )
            showresulttime+=1
