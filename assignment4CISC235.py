#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:35:38 2019

@author: graceziegler
"""

import random
from collections import defaultdict
from heapq import *


#generate random graph
def random_graph_generator(n):
    S = [1]
    #list of edges
    edges_list = []
    #list to hold existing edges
    existing = []
    for i in range(2,n):
        x = random.randint(1,i-1)
        S.append(random.randint(1,i-1))
        for s in S:
            #generate random weight
             w = random.randint(10,100)
             existing_edge = (str(i), str(s))
             #check to see if edge already exists
             if existing_edge not in existing: 
                 #if it does not, add it to list of edges
                 #and list of existing edges
                existing.append(existing_edge)
                edge = (str(i),str(s),w)
                edges_list.append(edge)
    return edges_list # return list of edges




def prims_alg( vertex, edges_list ):
    total_weight = 0
    connections = defaultdict( list ) #connections
    for v1,v2,c in edges_list: 
        connections[ v1 ].append( (c, v1, v2) ) 
        connections[ v2 ].append( (c, v2, v1) ) 
    mst = [] #MST tree
    visited_v = []
    visited_v.append(vertex)#list of visited vertices
    #possible edges to be used
    poss_edges = connections[ vertex ][:]
    heapify( poss_edges )
 
    while poss_edges: #While there are still usable edges
        cost, v1, v2 = heappop( poss_edges )
        if v2 not in visited_v: 
            visited_v.append( v2 ) 
            mst.append( ( v1, v2, cost ) )
            for e in connections[ v2 ]:
                if e[ 2 ] not in visited_v:
                    heappush( poss_edges, e )
    for i in mst:  #Print the tree and get the total weight.
        total_weight += i[2]
    return total_weight




#modified bfs algorithm
def breadth_first(lis, v):
    #empty queue
    Q = [] 
    first = v
    #path taken in graph
    path_taken = []
    new_list = []
    visited_v = [] #list to hold visited vertices
    total_weight = 0 #Total Wieght
    Q.append([first]) 
    visited_v.append(first) #Mark as visited
    current = first
    for i in lis:
        new_list.append((i[1],i[0],i[2]))  #Add the edges
    lis.extend(new_list)
    lis.sort()
    for j in lis:
        #find the starting vertex in lis
        if j[0]==v: 
            #add this vertex to the path
            path_taken.append(j) 
    for x in path_taken:
        #iterate through items in the path
        if x[1] not in visited_v: 
            #if not yet visited
            visited_v.append(x[1]) #mark as visited
            #add to the queue
            Q.append(x[1])
            total_weight += x[2]
    #remove from the queue
    Q.pop(0)
    #current node in queue
    current = Q[0]
    #while the queue is not empty
    while Q: 
        #iterate through lis
        for s in lis:
            #if s[0] is our current node in queue
            if s[0] == current:
                path_taken.append(s) #add to path
        #iterate through our path
        for n in path_taken:
            if n[1] not in visited_v:
                visited_v.append(n[1]) #mark it visited
                Q.append(n[1]) #add to queue
                total_weight += n[2] #add the edges weight
        Q.pop(0)
        if len(Q) != 0:
            current = Q[0]
        else:
            return total_weight





#create the graph
edges_list = [("0", "0", 0),("0", "1", 15),("0","2",0),("0", "3", 7),("0", "4", 10),("0", "5", 0),("1", "1", 0), ("2", "2", 0),("3", "3", 0), ("4", "4", 0),("5", "5", 0),("1", "0", 15),
          ("1", "2", 0),("1", "3", 11),("1", "4", 0), ("1", "5", 9),("2", "0", 0), ("2", "1", 9),("2", "3", 0), ("2", "4", 12),("2", "5", 7),("3", "0", 7),("3", "1", 11),("3", "2", 0),
          ("3", "4", 8),("3", "5", 14),("4", "0", 10),("4", "1", 0),("4", "2", 12), ("4", "3", 8),("4", "5", 8), ("5", "0", 0),("5", "1", 9),("5", "2", 7),("5", "3", 14),("5", "4", 8)]

vertex = random.randint(0,6)
vertex = str(vertex)
print ("Prim:", prims_alg(vertex, edges_list ))
print ("BFS:", breadth_first(edges_list, vertex))
print ("\n")


ns = [20,40,60]
for n in ns:
    print ("DIFF: ",n)
    for i in range(10):
        g = random_graph_generator(n)
        randomVertex = random.randint(1,n-1)
        randomVertex = str(randomVertex)
        bfs = breadth_first(g,randomVertex)
        bfs = float(int(bfs))
        prim = prims_alg(randomVertex,g)
        prim = float(int(prim))
        ratio = bfs-prim
        ratio = ratio/prim
    print("BFS - Prims = ", bfs, "-", prim, "= ", bfs-prim)
    print(ratio, "or ", ratio*100,"%")
