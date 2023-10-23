from typing import List, Tuple
INF = 0x3f3f3f3f
 
# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, V: int):
        # No. of vertices
        self.V = V
         
        # In a weighted graph, we need to store vertex and weight pair for every edge
        self.adj = [[] for _ in range(V)]
 
    # function to add an edge to graph
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
 
    # Prints shortest paths from src to all other vertices.
    # W is the maximum weight of an edge
    def shortestPath(self, src: int, W: int):
        # With each distance, iterator to that vertex in its bucket is stored so that vertex can be deleted
        # in O(1) at time of updation. So dist[i][0] = distance of ith vertex from src vertex
        # dist[i][1] = iterator to vertex i in bucket number
        dist = [[INF, None] for _ in range(self.V)]
 
        # Initialize distance of source vertex
        dist[src][0] = 0
 
        # Create buckets B[].
        # B[i] keep vertex of distance label i
        B = [[] for _ in range(W * self.V + 1)]
        B[0].append(src)
 
        idx = 0
        while True:
            # Go sequentially through buckets till one non-empty bucket is found
            while len(B[idx]) == 0 and idx < W * self.V:
                idx += 1
 
            # If all buckets are empty, we are done.
            if idx == W * self.V:
                break
 
            # Take top vertex from bucket and pop it
            u = B[idx][0]
            B[idx].pop(0)
 
            # Process all adjacents of extracted vertex 
            # 'u' and update their distances if required.
            for v, weight in self.adj[u]:
                du = dist[u][0]
                dv = dist[v][0]
 
                # If there is shorted path to v through u.
                if dv > du + weight:
                    # If dv is not INF then it must be in 
                    # B[dv] bucket, so erase its entry using iterator
                    # in O(1)
                    if dv != INF:
                        B[dv].remove(v)
 
                    # updating the distance
                    dist[v][0] = du + weight
                    dv = dist[v][0]
 
                    # pushing vertex v into updated distance's bucket
                    B[dv].append(v)
 
                    # storing updated iterator in dist[v][1]
                    dist[v][1] = len(B[dv]) - 1
 
        # Print shortest distances stored in dist[]
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}     {dist[i][0]}")
 
# Driver program to test methods of graph class
def main():
    # create the graph given in above figure
    V = 9
    W = 14
    g = Graph(V)
 
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
 
    g.shortestPath(0, W)
 
if __name__ == "__main__":
    main()
