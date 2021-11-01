import math 

def setEmptyGraph(size):
  n = size*size
  G = [ [] for _ in range(n) ]
  for x in range(size):
    for y in range(size):
      if(size > x + 1):
        G[ ((x * size) + y) ].append(((x+1) * size) + y)
      if(0 <= x - 1):
        G[ ((x * size) + y) ].append(((x-1) * size) + y)
      if(size > y + 1):
        G[ ((x * size) + y) ].append((x * size) + (y+1))
      if(0 <= y - 1):
        G[ ((x * size) + y) ].append((x * size) + (y-1))
  return G

def setKnownPoints(size, almacen, entrega):
  id = ["Null"]*(size*size) #0 is null
  for a in almacen:
    x, y = a[0], a[1]
    pos = x*size + y # function to get position by x and y
    id[pos] = "A" # 1 is almacen
  for a in entrega:
    x, y = a[0], a[1]
    pos = x*size + y # function to get position by x and y
    id[pos] = "E" # 2 is delivery node
  return id

def getGraphWeighted(G):
  adjlListWeighted = [[] for i in range(len(G))]
  for i in range(len(G)):
    for j in range(len(G[i])):
      adjlListWeighted[i].append( ( G[i][j], round(math.sqrt( ( i%(len(G)/2)- G[i][j]%(len(G)/2) ) **2 + ( i // (len(G)/2) - G[i][j] // (len(G)/2)) **2) )) )
  return adjlListWeighted
