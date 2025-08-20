import time

import torch
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

def torch_sierpinski_triangle(size):
    # Create a 2D grid of coordinates
    x = torch.arange(size).view(-1, 1) # column vector
    y = torch.arange(size).view(1, -1) # row vector

    # Bitwise AND of x and y being 0 defines the Sierpinski pattern
    triangle = ((x & y) == 0).int()

    return triangle

def naive_sierpinski_triangle(size):
    return [[(x & y) == 0 for x in range(size)] for y in range(size)]


size = 8192  # Must be a power of 2

triangle_tensor = torch_sierpinski_triangle(size)

plt.ion()
plt.imshow(triangle_tensor, cmap='binary')
plt.show(block=True)


