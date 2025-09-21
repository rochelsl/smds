# Class for animating the MD simulation in 2D using matplotlib and FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from MDSimulation2D import MDSimulation2D
import numpy as np
from matplotlib.patches import Circle

class Animation2D:
    def __init__(self, sim: MDSimulation2D, interval=100):
        self.sim = sim
        self.interval = interval
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('X [nm]')
        self.ax.set_ylabel('Y [nm]')
        self.ax.set_title('2D MD Simulation')
        self.ax.set_xlim(0, sim.box_size)
        self.ax.set_ylim(0, sim.box_size)
        self.ax.set_aspect('equal', 'box')

        particles = np.array([self.sim.get_particles()]).flatten()
        self.circles = []
        for p in particles:
            c = Circle((p.getX(), p.getY()),
                       radius=p.get_Radius(),
                       facecolor="black",
                       edgecolor='None', animated=True)
            self.ax.add_patch(c)
            self.circles.append(c)

        self.ani = FuncAnimation(self.fig, self.update, init_func=self.init, interval=self.interval, blit=True)
        
    def init(self):
        return tuple(self.circles)
    
    def update(self, frame):
        self.sim.timestep_LJ()
        for p, c in zip(self.sim.get_particles(), self.circles):
            c.center = (p.getX(), p.getY())   # keep radius/color; just move
        return tuple(self.circles)
    
    def show(self):
        plt.show()