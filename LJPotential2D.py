# This class is used for calculating the Lennard-Jones potential between two particles
class LJPotential2D:
    def __init__(self, epsilon=1.0, sigma=1.0): # constructor with default values
        self.epsilon = epsilon
        self.sigma = sigma

    def calculate(self, r): # calculate the Lennard-Jones potential given distance r
        #if r == 0:
        #    return float('inf') # avoid division by zero
        sr6 = (self.sigma / r) ** 6
        sr12 = sr6 ** 2
        return 4 * self.epsilon * (sr12 - sr6)
    
    def __repr__(self): # official string representation
        return f'LJPotential2D(epsilon={self.epsilon}, sigma={self.sigma})'