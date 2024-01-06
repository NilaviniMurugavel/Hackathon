import json
import numpy as np 
import pandas as pd
 
 
f = open("C:/21pd22-Hackathon/Input data/level0.json")
 
 
 
data = json.load(f)
 
 
#print(data)
#print(data["neighbourhoods"])
 
f.close()

print(data['restaurants'])
print(data['vehicles'])
temp=data['restaurants']['r0']['neighbourhood_distance']
print("------------")
print(temp)
distance_matrix=[]
distance_matrix.append(data['restaurants']['r0']['neighbourhood_distance'])
distance_matrix[0].insert(0,0)
print("------------")
print(distance_matrix)
print("------------")
val=1
for i in data['neighbourhoods']:
    t=data['neighbourhoods'][i]['distances']
    t.insert(0,temp[val])
    val=val+1
    #print(t)
    distance_matrix.append(t)
for i in distance_matrix:
    print(i)
  

res=[]
def travellingsalesman(c):
    global cost
    adj_vertex = 999
    min_val = 10000
    visited[c] = 1
    print((c + 1), end=" ")
    res.append(c-1)
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 10000:
        cost = cost + min_val
    if adj_vertex == 999:
        adj_vertex = 0
        print((adj_vertex+1), end=" ")
        
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
n = 21
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array(distance_matrix)
print("Shortest Path:", end=" ")
travellingsalesman(0)
print()

print(res)
res1=[]
res1.append('r0')
for i in range (1,len(res)):
    s='n'+str(res[i])
    res1.append(s)
res1.append('r0')
print(res1)
result={'v0': {'path':res1}}
with open("OutputLevel0.json", "w") as outfile:
    json.dump(result, outfile)
