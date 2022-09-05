#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getSortedWorkers' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING data as parameter.
#
from collections import deque

allPeople = dict()
finalCosts = dict()
graph = dict()

def recurCalc(currentNodeName, currentLevel):
    if currentNodeName in graph.keys():
        for node in graph[currentNodeName]:
            finalCosts[node] += int(allPeople[currentNodeName][1]) + currentLevel + recurCalc(node, currentLevel+1)
    return 0
    

def mainFunction(data):
    # Write your code here
    data = data.split(",")
    for d in data:

        splitStr = d.split(" ")

        allPeople[splitStr[0]] = (splitStr[1], splitStr[2])
        if splitStr[1] not in graph.keys():
            graph[splitStr[1]] = set()
        graph[splitStr[1]].add(splitStr[0])
    print(graph)
    
    for node in allPeople:
        finalCosts[node] = 0
    
    for node in graph["None"]:
        finalCosts[node] += recurCalc(node, 0)
    
    finalList = dict(sorted(finalCosts.items(), key = lambda item: (item[1], item[0])))

    print(finalList)
    
    finalString = ''
    
    for f in finalList:
        finalString += f + '\n'
    return finalString.strip()
    
