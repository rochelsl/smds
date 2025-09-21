# Run the MD simulation using the classes MDSimulation2D and LJPotential2D of point-like particles in 2D (class: Particle2D)
# Render the simulation using Animation2D class
from MDSimulation2D import MDSimulation2D
#from LJPotential2D import LJPotential2D
from Animation2D import Animation2D
#from Particle2D import Particle2D

def run_simulation(num_particles=10, particle_radius=0.5, box_size=100.0, num_steps=100, dt=0.01, temperature=1, epsilon=1.0, sigma=1.0):
    sim = MDSimulation2D(num_particles, particle_radius, box_size, dt=dt, temperature=temperature, epsilon=epsilon, sigma=sigma)
    sim.initialize_particles()
    sim.initial_velocities()
    
    print("Initial Configuration:")
    for config in sim.current_configuration():
        print(config)
    
    print("\nInitial Velocities:")
    for vel in sim.current_velocities():
        print(vel)
    
    ani = Animation2D(sim, interval=100)
    ani.show()
    
    for step in range(num_steps):
        sim.timestep_LJ()  # uses sim.dt and sim.lj
    
    print("\nFinal Configuration after {} steps:".format(num_steps))
    for config in sim.current_configuration():
        print(config)
    
    print("\nFinal Velocities after {} steps:".format(num_steps))
    for vel in sim.current_velocities():
        print(vel)
if __name__ == "__main__":
    run_simulation(num_particles=100, particle_radius=0.5, box_size=20.0, num_steps=1, dt=0.0001, temperature=100, epsilon=2, sigma=2)