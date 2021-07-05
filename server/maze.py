from random import randint, sample
from sys import argv

class maze:
    def __init__(self):
        self.parent = list(range(20*20))
        self.rank = [0] * len(self.parent)

    def find(self,n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]


    def union(self,a, b):
        u, v = self.find(a), self.find(b)
        if u == v:
            return
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[u] = v
            if self.rank[v] == self.rank[u]:
                self.rank[v] += 1

    def get_coords(self,num):
        return num // 20, num % 20

    def create(self):
        edges_of_cells = {
            edge for num in self.parent[:-1]
            for edge in ((num, num+1), (num, num+20))
            if not (edge[0] % 20 == 20-1 and edge[1]-edge[0] < 20) and \
                edge[1] <= self.parent[-1]
            }
            
        maze = set()
        # Display initial state of maze
        #disp_maze(width, height, maze, 0)

        # while there is more than 1 set of connected cells
        while len(set([self.find(n) for n in self.parent])) > 1:
            rand_edge = sample(edges_of_cells, 1)[0]
            edges_of_cells.remove(rand_edge)
            u, v = self.find(rand_edge[0]), self.find(rand_edge[1])
            if u != v:
                self.union(u, v)
            else:
                maze.add((self.get_coords(rand_edge[0]), self.get_coords(rand_edge[1])))

        
        while edges_of_cells:
            maze.add(tuple(self.get_coords(num) for num in edges_of_cells.pop()))
        return maze

