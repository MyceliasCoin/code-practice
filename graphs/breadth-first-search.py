# Print BFS traversal from a given source vertex
# BFS(int s) traverses vertices reachable from s
from collections import defaultdict


# class represents a directed graph using adjacency list representation
class Graph:

    # constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add edge to a graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # function to print BFS given starting vertex
    def breadth_first_search(self, s):

        # mark all vertices as not yet visited
        visited = [False] * len(self.graph)

        # create queue
        queue = []

        # mark source node as visited and enqueue
        queue.append(s)
        visited[s] = True

        while queue:

            # dequeue vertex and print out
            s = queue.pop(0)
            print(s, end=" ")

            # get all adjacent vertices of dequeued vertex s
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


# driver script
if __name__ == "__main__":

    # create binary tree
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is BFS starting from vertex 2")

    g.breadth_first_search(2)
