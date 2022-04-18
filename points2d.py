from matplotlib import pyplot as plt
import numpy as np
from math import pi

class Points2D:
    def __init__(self, n):
        self.n = n
        self.points = np.array([[np.random.uniform(0.0, 1.0, 1), np.random.uniform(0.0, 1.0, 1)] for _ in range(n)])
        self.distances = [(point[0]**2 + point[1]**2)**0.5 for point in self.points]

    def get_num(self):
        return self.n

    def get_points(self):
        return self.points

    def regenerate(self):
        self.points = np.random.rand(self.n, 2)

    def approximate(self):
        count = 0
        for distance in self.distances:
            if distance <= 1:
                count += 1
        return count / len(self.points)

    def _gen_colors(self):
        cols = []
        for distance in self.distances:
            if distance <= 1:
                cols.append( (0,0,1,1) )
            else:
                cols.append( (1,0,0,1) )
        return cols

    def plot(self):
        cols = self._gen_colors()
        figure, axes = plt.subplots()

        axes.set_xlim(0.0,1.0)
        axes.set_ylim(0.0,1.0)
        axes.set_xlabel("x")
        axes.set_ylabel("y")

        approx = self.approximate() * 4
        error = ((pi - approx) / pi)*100
        title = "π ≈ " + str(approx) + "\n n = " + str(len(self.points)) + "\n error = " + str(error) + "%"

        axes.set_title(title)
        plt.scatter(self.points[:,0], self.points[:,1],s=3,c=cols)
        circ = plt.Circle((0,0), 1, color=(0,0,0,0.25))
        axes.add_artist(circ)
        plt.show()
        return None
