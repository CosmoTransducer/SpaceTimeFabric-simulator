<h1 align="center">SpaceTimeFabric-simulator</h1>



<div style="display: flex; align-items: flex-start; gap: 20px;">
  <div style="flex: 2;">
    Visualization of how mass warps spacetime, inspired by Einstein's General Theory of Relativity —  
    explained using the classic "rubber sheet" analogy and simulated in Python using `matplotlib`.
  </div>
</div>
  
  <br/>
<div>  
  <div style="flex: 1;">
    <img src="https://github.com/user-attachments/assets/612d0a63-2c65-4b07-909e-79b44b3d0340" alt="space-time fabric" width="100%" style="border-radius: 12px; box-shadow: 0 0 10px rgba(0,0,0,0.2);" />
  </div>
</div>

<br/>

### General Theory of Relativity

> In simple words, **mass and energy tell spacetime how to curve**, and **curved spacetime tells matter how to move**.

The **greater the mass** (or concentrated energy), the **deeper the curve** in the space-time fabric — resulting in a **stronger gravitational pull**.

---

### Key Requirements

* Simulate **mass and energy** in 2D space
* Show how one object affects another (i.e., simulate **relativity**)
* Represent **time dilation** based on the curve intensity
* Solid understanding of **Python + NumPy + Matplotlib**
* Clear grasp of **general relativity**

---

### Basic Approach

1. **Create a 2D grid** representing space: `X`, `Y`
2. Add **mass at the center** (or anywhere on the grid)
3. Apply a **gravitational potential function** to warp the grid:

```math
Z(x, y) = - \frac{G \cdot M}{\sqrt{(x - x_0)^2 + (y - y_0)^2 + \varepsilon}}
```

Where:

* `G`: gravitational constant (set to 1 for simplicity)
* `M`: mass value
* `(x₀, y₀)`: coordinates of the mass
* `ε`: a small value to avoid division by zero

4. Use a **3D surface plot** (`matplotlib`) to visualize space-time curvature.

---

### Setup Requirements

```bash
pip install numpy matplotlib
```


---


<p align="center">
  <a href="https://github.com/dhairyajangir" target="_blank" rel="noopener noreferrer">
    <img src="https://github.com/user-attachments/assets/d7d09299-1286-43b9-a59e-42825105f7a9" alt="spiral" width="150"/>
  </a>
</p>

