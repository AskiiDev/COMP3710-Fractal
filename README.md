# Sierpinski Triangle Fractal Implementation

A PyTorch-based implementation of the Sierpinski Triangle fractal using bitwise operations for efficient parallel computation.

## Overview

The Sierpinski Triangle is a famous fractal named after Polish mathematician Wacław Sierpiński. It's a self-similar fractal that can be constructed through various methods. This implementation uses the elegant bitwise AND property: a point (x,y) is part of the triangle if and only if `(x & y) == 0` in binary representation.

## Requirements

```python
torch>=1.9.0
matplotlib>=3.3.0
numpy
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/sierpinski-triangle-pytorch.git
cd sierpinski-triangle-pytorch
```

2. Install dependencies:
```bash
pip install torch matplotlib numpy
```

## Usage

### Basic Usage

```python
import torch
import matplotlib.pyplot as plt

# Set device (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Generate Sierpinski Triangle
size = 1024  # Must be a power of 2
triangle = torch_sierpinski_triangle(size)

# Display the fractal
plt.imshow(triangle, cmap='binary')
plt.show()
```

### Performance Comparison

The implementation includes both a PyTorch-optimized version and a naive Python version:

- `torch_sierpinski_triangle(size)`: Vectorized PyTorch implementation
- `naive_sierpinski_triangle(size)`: Pure Python implementation for comparison

## Algorithm Explanation

The Sierpinski Triangle can be generated using the binary representation property:
- For each point (x, y) in the grid
- Compute the bitwise AND: `x & y`
- If the result equals 0, the point belongs to the triangle
- Otherwise, it's part of the background

This method leverages the fractal's self-similar nature and Pascal's Triangle modulo 2.

## Code Structure

```
sierpinski_triangle.py
├── torch_sierpinski_triangle()  # Main PyTorch implementation
├── naive_sierpinski_triangle()  # Reference Python implementation
└── Main execution block          # Demo and visualization
```

## Acknowledgments

- Created for COMP3710 Pattern Analysis Lab 1
- Inspired by Wacław Sierpinski's mathematical work