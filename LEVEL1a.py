import json
import numpy as np 
import pandas as pd
 
 
f = open("C:/21pd22-Hackathon/Input data/level1a.json")
 
 
 
data = json.load(f)
 
capacity=[] 
#print(data)
print(data["vehicles"])
for i in data['neighbourhoods']:
    print(i,data['neighbourhoods'][i]['order_quantity'])
    capacity.append(data['neighbourhoods'][i]['order_quantity'])
f.close()
# Python3 Program for Floyd Warshall Algorithm
temp=data['restaurants']['r0']['neighbourhood_distance']
print("------------")
 
distance_matrix=[]
distance_matrix.append(data['restaurants']['r0']['neighbourhood_distance'])
distance_matrix[0].insert(0,0)
val=1
for i in data['neighbourhoods']:
    t=data['neighbourhoods'][i]['distances']
    t.insert(0,temp[val])
    val=val+1
    #print(t)
    distance_matrix.append(t)

# Number of vertices in the graph
V = 21

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Solves all pair shortest path
# via Floyd Warshall Algorithm
sdist=[]

def floydWarshall(graph):
	""" dist[][] will be the output 
	matrix that will finally
		have the shortest distances 
		between every pair of vertices """
	""" initializing the solution matrix 
	same as input graph matrix
	OR we can say that the initial 
	values of shortest distances
	are based on shortest paths considering no 
	intermediate vertices """

	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

	""" Add all vertices one by one 
	to the set of intermediate
	vertices.
	---> Before start of an iteration, 
	we have shortest distances
	between all pairs of vertices 
	such that the shortest
	distances consider only the 
	vertices in the set 
	{0, 1, 2, .. k-1} as intermediate vertices.
	----> After the end of a 
	iteration, vertex no. k is
	added to the set of intermediate 
	vertices and the 
	set becomes {0, 1, 2, .. k}
	"""
	for k in range(V):

		# pick all vertices as source one by one
		for i in range(V):

			# Pick all vertices as destination for the
			# above picked source
			for j in range(V):

				# If vertex k is on the shortest path from
				# i to j, then update the value of dist[i][j]
				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
	 
	printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
	
	print("Following matrix shows the shortest distances\
between every pair of vertices")
	for i in dist:
		print(i,"\n")
		sdist.append(i)


# Driver's code
if __name__ == "__main__":
	 
	graph = distance_matrix
	# Function call
	#floydWarshall(graph)
	
"""print("\n\n----------------------\n")
print(sdist[0])
print(capacity)
for i in range(1,len(sdist[0])):
	print(i,sdist[0][i]/capacity[i-1])"""
capacity.insert(0,1)
result=[]
count=0
visited=[]
ratio=[]
for i in distance_matrix:
 res=[]
 for j in range(len(i)):
    res.append(round( i[j] / capacity[j],3))
 ratio.append(res)
print(ratio)
visited=[0]
count=0
start=0
node=start
totalCap=0
pF=[]
p=[]
while(count<21):
    t=ratio[node]
    for i in visited:
      t[i]=0
    if 0 in t:
      t = [i for i in t if i != 0]
    if len(t)==0:
        pF.append(p)
        break
    minV=min(t)
     
    #ind=distance_matrix[node].index(minV)
    ind=ratio[node].index(minV)
    visited.append(ind)
    #print(visited)
    currCap=capacity[ind]
    if(totalCap+currCap<=600):
        totalCap=totalCap+currCap
        node=ind
        count=count+1
        print(node)
        p.append(node)
    else:
        pF.append(p)
        p=[]
        print(totalCap)
        node=start
        totalCap=0
        print("--------------------------")
print(pF)
for i in range(0,len(pF)):
    for j in range(0,len(pF[i])):
        pF[i][j]=pF[i][j]-1
#print(pF)
result=[]
for i in pF:
     lt=[]
     for j in i:
        lt.append('n'+str(j))
     result.append(lt)
#print(result)
for i in result:
     i.insert(0,'r0')
     i.append('r0')
print(result)
r={'v0': {'path1':result[0],'path2':result[1],'path3':result[2]}}
with open("OutputLevel1a.json", "w") as outfile:
    json.dump(r, outfile)
		
	