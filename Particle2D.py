from Point2D import *

class Particle2D(Point2D):
    def __init__(self, x_Pos=0, y_Pos=0, radius=0.1, mass=1.0): # constructor with default values
        super().__init__(x_Pos, y_Pos)
        self.mass = mass
        self.radius = radius

    def set_mass(self, mass): # set the mass
        self.mass = mass
    
    def get_mass(self): # get the mass
        return self.mass
    
    def set_Radius(self, radius): # set the radius
        self.radius = radius

    def get_Radius(self): # get the radius
        return self.radius

    def __str__(self): # string representation
        return f'Particle2D at ({self.x_Pos}, {self.y_Pos}), with mass {self.mass}'
    
    def __repr__(self): # official string representation
        return f'Particle2D(x={self.x_Pos}, y={self.y_Pos}, mass={self.mass})'
