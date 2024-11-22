README.md - 0x07. Rotate 2D Matrix
Project Overview
In this project, you will implement an algorithm to rotate a given n x n 2D matrix 90 degrees clockwise. The task involves manipulating a matrix in place, meaning that you will modify the original matrix without creating any additional copies.

The matrix will be represented as a list of lists in Python, and the rotation should be performed without using extra space beyond the original matrix.

Concepts Covered
1. Matrix Representation in Python
You will be working with a 2D matrix represented as a list of lists in Python.
Understanding how to access and modify elements within a 2D matrix is crucial for this task.
2. In-place Operations
An in-place operation modifies the data structure without creating a copy.
The goal is to rotate the matrix 90 degrees without using additional memory beyond the matrix itself.
3. Matrix Transposition
A key part of rotating a matrix is transposing it, which involves swapping rows with columns.
You'll need to transpose the matrix as a step in the rotation process.
4. Reversing Rows
After transposing, reversing the rows is another critical step to complete the 90-degree clockwise rotation.
5. Nested Loops
You will use nested loops to iterate over the matrix and apply the necessary transformations at each step.
Project Requirements
Prototype: def rotate_2d_matrix(matrix):
Input: An n x n 2D matrix.
Output: The matrix should be rotated in-place (no return value).
Constraints:
The matrix is guaranteed to be 2D and non-empty.
No external libraries or modules are allowed.
Your code should follow the PEP 8 style guide.
Ensure your code is well-documented.
Allowed Editors
vi, vim, emacs
Environment
Ubuntu 20.04 LTS with Python 3.8.10
Interpreter: Python 3 (#!/usr/bin/python3)
Code Documentation
All functions and modules must be documented.
Task
0. Rotate 2D Matrix (Mandatory)
Task: Rotate an n x n matrix 90 degrees clockwise.
Function Prototype: def rotate_2d_matrix(matrix):
Details: The matrix must be edited in-place without returning anything.
Example:
python
Copy code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
Output:

python
Copy code
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
Approach
To rotate the matrix 90 degrees clockwise, you can follow these steps:

Transpose the Matrix: Swap the rows and columns.
Reverse Each Row: After transposing, reverse each row to complete the 90-degree rotation.
Step-by-Step Process:
Transpose:

Loop through each element of the matrix and swap the elements at position (i, j) with (j, i).
Reverse Rows:

After transposing, reverse each row of the matrix to finalize the 90-degree clockwise rotation.
Example Walkthrough
Given the matrix:

python
Copy code
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Transpose:
python
Copy code
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
Reverse Each Row:
python
Copy code
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
Testing
You can test your implementation with the provided example:

python
Copy code
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
Expected output:

python
Copy code
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Resources
Python Official Documentation: Learn about lists and list manipulation in Python.
GeeksforGeeks: Articles on matrix transposition and in-place matrix rotation.
TutorialsPoint: Python lists and basic list manipulation techniques.
Additional Requirements
Auto QA Review: A review will be conducted at the project deadline, and your code will be evaluated based on its correctness, efficiency, and style.
Conclusion
By completing this project, you will gain valuable experience in working with 2D matrices, performing in-place operations, and solving algorithmic problems efficiently. This challenge not only enhances your Python programming skills but also improves your understanding of matrix manipulation and space optimization techniques.
