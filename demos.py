import matplotlib.pyplot as plt 
import numpy as np
import random

class GridIllustration():
    def __init__(self, N: int, p: float) -> None:
        self.dimensions = (N,N)
        self.p = p
        self.identities = np.zeros(self.dimensions)
    
    def get_neighbours(self, coord):
        row, col = tuple(coord)
        neighbours = [(row, col+1), (row-1, col), (row, col-1), (row+1, col)]
        neighbours = [coord for coord in neighbours if (coord[0] >=0 and coord[1]>=0 and coord[0]<self.dimensions[0] and coord[1]<self.dimensions[1])]
        return neighbours

    def grow_from_seed_FIFO(self, seed_coords: tuple):
        self.identities[seed_coords] = 2.0
        occupied = [seed_coords]
        vacant = []
        visited = [seed_coords]
        queue = [seed_coords]
        while queue != []:
            site = queue.pop(0)
            visited.append(site)
            for neighbour in self.get_neighbours(site):
                if neighbour not in visited:
                    visited.append(neighbour)
                    if random.random() <= self.p: #r.pop(0) ==1 :
                        occupied.append(neighbour)
                        self.identities[neighbour] = 1.0
                        queue.append(neighbour)
                    else:
                        vacant.append(neighbour)
                        self.identities[neighbour] = 0.0

    def display(self):
        fig, ax = plt.subplots()
        plt.imshow(self.identities)
        ax.set_xticks([])
        ax.set_yticks([])
