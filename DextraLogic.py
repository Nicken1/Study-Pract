import sys
def dijkstra(src,c,l,k,city_labels,n,W):
        x=""
        graph=W
        V=n
        dist = [sys.maxsize] * V
        dist[src] = 0
        if len(c)>0:
            if c.count(src)>0:
                for f in range (V):
                    dist[f]=0
            else:
                for f in range (len(c)):
                    dist[c[f]]=0
        if len(k)==1 and k[0]==src:
          i=0
          for f in range (V):
              if i==l[0] or i==k[0]:
                 i=i+1
              elif i!=l[0] or i!=k[0]:
                   dist[i]=0
                   i=i+1

        sptSet = [False] * V

        for cout in range(V):
            min = sys.maxsize
            for v in range(V):
                if dist[v] < min and sptSet[v] == False: 
                    min = dist[v]
                    min_index = v
            u = min_index
            print(u)
            sptSet[u] = True
 
            for v in range(V):
               
                    if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
        print("Кратчайшии пути")
        for node in range(V):
            if dist[node]==sys.maxsize:
                dist[node]=0
                x+=city_labels[node]+" "+"Путь = "+str(dist[node])+"<br>"
            else:
                x+=city_labels[node]+" "+"Путь = "+str(dist[node])+"<br>"
        return x
