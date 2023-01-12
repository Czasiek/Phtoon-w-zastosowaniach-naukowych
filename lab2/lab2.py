import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm
import imageio.v2 as imageio



class IsingModel:
    def __init__(self, size, temp):
        self.size = size
        self.temp = temp
        self.lattice = np.random.choice([-1, 1], size=(size, size))

    def energy(self, i, j):
        return - self.lattice[i, j] * (self.lattice[i, (j+1)%self.size] + self.lattice[i, (j-1)%self.size] + self.lattice[(i+1)%self.size, j] + self.lattice[(i-1)%self.size, j])

    def monte_carlo(self, steps):
        for step in tqdm(range(steps)):
            i, j = np.random.randint(0, self.size, 2)
            delta_e = 2 * self.lattice[i, j] * self.energy(i, j)
            if delta_e <= 0 or np.random.random() < np.exp(-delta_e / self.temp):
                self.lattice[i, j] *= -1
            self.save_lattice(step)
            self.save_magnetization(step)

    def save_lattice(self, step):
        plt.imshow(self.lattice, cmap='coolwarm')
        plt.title(f'Step {step}')
        plt.savefig(f'step{step}.png')

    def save_magnetization(self, step):
        magnetization = np.sum(self.lattice) / (self.size * self.size)
        with open(f'magnetization{step}.txt', 'w') as f:
            f.write(str(magnetization))

    def create_gif(self):
        images = []
        for i in range(steps):
            images.append(imageio.imread(f'step{i}.png'))
        imageio.mimsave('ising_simulation.gif', images)

# usage 
size = 3
temp = 2.27
steps = 10

simulation = IsingModel(size, temp)
simulation.monte_carlo(steps)
simulation.create_gif()
