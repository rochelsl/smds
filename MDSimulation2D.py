from Particle2D import Particle2D
from LJPotential2D import LJPotential2D
import random

class MDSimulation2D:
    def __init__(self, num_particles=10, particle_radius=0.5, box_size=100.0, dt=0.01, temperature=1, epsilon=1.0, sigma=1.0): # constructor with default values
        self.num_particles = num_particles
        self.box_size = box_size
        self.dt = dt
        self.temperature = temperature
        self.particle_radius = particle_radius
        # single LJ instance reused every step
        self.lj = LJPotential2D(epsilon=epsilon, sigma=sigma)
        self.calculate_LJ = self.lj.calculate

    def get_particles(self): # get the list of particles
        return self.particles
    
    def set_particles(self, particles): # set the list of particles
        self.particles = particles
        self.num_particles = len(particles)

    def initialize_particles(self, min_gap_factor=1.1, max_tries=10_000):
        particles = []
        L = self.box_size
        halfL = 0.5 * L

        for _ in range(self.num_particles):
            for _try in range(max_tries):
                x = random.uniform(0.0, L)
                y = random.uniform(0.0, L)

                ok = True
                for p in particles:
                    min_dist = (2 * p.get_Radius()) * min_gap_factor
                    dx = x - p.getX()
                    dy = y - p.getY()
                    dx = (dx + halfL) % L - halfL
                    dy = (dy + halfL) % L - halfL
                    if dx*dx + dy*dy < min_dist*min_dist:
                        ok = False
                        break

                if ok:
                    particles.append(Particle2D(x_Pos=x, y_Pos=y,
                                                radius=self.particle_radius,
                                                mass=random.uniform(1.0, 10.0)))
                    break
            else:
                raise RuntimeError(
                    "Could not place all particles without overlap. "
                    "Reduce density or min_gap_factor, or increase box_size."
                )

        self.particles = particles

        
    def current_configuration(self): # return current configuration of particles
        return [(p.getX(), p.getY(), p.get_mass()) for p in self.particles]
    
    def initial_velocities(self): # assign initial random velocities to particles
        self.velocities = [(random.uniform(-1*self.temperature, 1*self.temperature), random.uniform(-1*self.temperature, 1*self.temperature)) for _ in range(self.num_particles)]
        return self.velocities
    
    def current_velocities(self): # return current velocities of particles
        return self.velocities if hasattr(self, 'velocities') else None

    def timestep_LJ(self, dt=None): # perform a single timestep using Lennard-Jones potential from the class LJPotential2D
        if dt is None:
            dt = self.dt
        forces = [(0.0, 0.0) for _ in range(self.num_particles)]
        for i in range(self.num_particles):
            for j in range(i + 1, self.num_particles):
                dx = self.particles[j].getX() - self.particles[i].getX()
                dy = self.particles[j].getY() - self.particles[i].getY()
                r = (dx**2 + dy**2)**0.5
                if r == 0:
                    continue
                f_mag = -self.calculate_LJ(r) / r
                fx = f_mag * dx
                fy = f_mag * dy
                forces[i] = (forces[i][0] + fx, forces[i][1] + fy)
                forces[j] = (forces[j][0] - fx, forces[j][1] - fy)
        for i in range(self.num_particles):
            ax = forces[i][0] / self.particles[i].get_mass()
            ay = forces[i][1] / self.particles[i].get_mass()
            vx, vy = self.velocities[i]
            max_speed = 100.0
            if self.velocities[i] > (max_speed, max_speed):  # avoid excessive speeds
                vx = max_speed * 0.5
                vy = max_speed * 0.5
            elif self.velocities[i] < (-max_speed, -max_speed):
                vx = -max_speed * 0.5
                vy = -max_speed * 0.5

            vx += ax * dt
            vy += ay * dt
            self.velocities[i] = (vx, vy)
            new_x = self.particles[i].getX() + vx * dt
            new_y = self.particles[i].getY() + vy * dt
            new_x = new_x % self.box_size
            new_y = new_y % self.box_size
            self.particles[i].setX(new_x)
            self.particles[i].setY(new_y)

    def __str__(self): # string representation
        return f'MDSimulation2D with {self.num_particles} particles in a box of size {self.box_size}'
    
    def __repr__(self): # official string representation
        return f'MDSimulation2D(num_particles={self.num_particles}, box_size={self.box_size}, particles={self.particles})'
