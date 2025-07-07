# SpaceTimeFabric-simulator
visualization of how mass warps spacetime, inspired by Einstein's general theory of relativity
explaination by simulating the classic "rubber sheet" analogy using Python and matplotlib

<img src="https://github.com/user-attachments/assets/612d0a63-2c65-4b07-909e-79b44b3d0340" alt="fabric" width="300"/>

###

### > general theory of relativity:
in simple words mass and energy tell spacetime how to curve, and curved spacetime tells matter how to move

higher the mass or higher the concentrated energy --> stronger and bigger the curve is --> means more stronger gravitational force of that object is


### 

### > key requirements 
- i need to simulate mass and energy 
- need to simulate how the object around other object behaves (relativity) 
- need to simulate the time too, which depends on how intense space-time fabric curve is  
- key understanding of python libs
- clear understanding of general theory of relativity

###
---

### > basic comman approach
1. **Create a 2D grid** to represent space `(X, Y)`.
2. Add **mass at the center** (or any point).
3. Use a **gravitational potential function** to warp the grid: ```Z(x, y) = -(G * M) / sqrt((x - x0)^2 + (y - y0)^2 + ε)```

<p align="center">
  <img src="https://github.com/user-attachments/assets/0031a818-8d28-4e80-8bb3-8a4fa2423a48" alt="fabric" width="300"/>
</p>

- Where:
  - `G` is the gravitational constant (can be set = 1 for simplicity),
  - `M` is the mass,
  - `(x0, y0)` is the position of the mass,
  - `ε` avoids division by zero.

4. Plot the result using **3D surface plot** to show how space is curved.


---
### > few key requirements to run this

```bash
pip install numpy matplotlib 
```


