0x09. Island Perimeter
Project Overview
The Island Perimeter project focuses on solving a geometric problem within a 2D grid. The goal is to compute the perimeter of an island, where the grid is represented as a list of lists of integers. This project challenges your understanding of algorithms, data structures, and Python programming principles.

Learning Objectives
Work with 2D arrays (matrices) to access and iterate over elements.
Use conditional logic to determine the contribution of individual cells to the perimeter.
Develop an algorithm to calculate and count edges of the island efficiently.
Apply Python programming skills, including nested loops and logical operations.
Requirements
Allowed editors: vi, vim, emacs.
Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
Code must follow PEP 8 style guidelines.
No external modules are allowed.
Each file must:
Start with #!/usr/bin/python3.
End with a new line.
Be executable.
Proper documentation is required for all functions.
Usage
Define the function island_perimeter(grid) in 0-island_perimeter.py.
Input:
grid: A list of lists of integers where:
0 represents water.
1 represents land.
Output:
Returns the perimeter of the island.
Example
Input:

python
Copy code
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
Output:

plaintext
Copy code
12
Task
Task 0: Write a function def island_perimeter(grid) that calculates the perimeter of the island in grid.
Constraints:
The grid is surrounded by water.
Only one island exists (no lakes or multiple islands).
The grid’s width and height do not exceed 100.
Repository Details
GitHub Repository: alx-interview
Directory: 0x09-island_perimeter
File: 0-island_perimeter.py
How to Run
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/alx-interview.git
cd 0x09-island_perimeter
Run the main program:
bash
Copy code
./0-main.py
Author: Nathan Baraka
Date: December 2024
