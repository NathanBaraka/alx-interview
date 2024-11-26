0x08. Making Change
Description
The "Making Change" project focuses on solving the classic coin change problem, a fundamental challenge in the domain of algorithms, particularly dynamic programming and greedy algorithms. The objective is to determine the minimum number of coins required to make up a given total using the provided denominations.

This project is designed to test your understanding of:

Algorithm design and optimization.
The principles of dynamic programming and greedy algorithms.
Python programming for solving computational problems.
Learning Objectives
Key Concepts:
Greedy Algorithms:

Understand how greedy strategies attempt to solve problems by making locally optimal choices.
Recognize the scenarios where greedy algorithms fail to find the global optimum.
Dynamic Programming:

Explore how dynamic programming can efficiently solve optimization problems.
Leverage concepts such as overlapping subproblems and optimal substructure.
Algorithmic Complexity:

Analyze the time and space complexity of your solution.
Strive for an efficient implementation that meets runtime constraints.
Problem-Solving Strategies:

Break down problems into smaller, manageable parts.
Compare iterative and recursive approaches for dynamic programming.
Python Programming:

Utilize Python lists, loops, and conditionals effectively.
Implement efficient algorithms using Python's robust feature set.
Requirements
Programming Environment:

All files must be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
Files must begin with the shebang: #!/usr/bin/python3.
Code should adhere to PEP 8 style (version 1.7.x).
Ensure that all files are executable and end with a new line.
Editor Choices: vi, vim, or emacs.

Tasks
0. Change Comes From Within
Prototype:

python
Copy code
def makeChange(coins, total):
Functionality:

Determine the fewest number of coins needed to make up the total amount using the provided list of coins.
Return:
0 if total is 0 or less.
-1 if the total cannot be met using the available coins.
Otherwise, the minimum number of coins required.
Assumptions:

Each coin value is a positive integer.
There is an infinite supply of each denomination.
Example Usage:

bash
Copy code
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
File Structure
GitHub Repository: alx-interview
Directory: 0x08-making_change
Files:
0-making_change.py: Contains the implementation of the makeChange function.
0-main.py: Example test file for validating your solution.
Resources
Python Documentation:

Control Flow Tools
GeeksforGeeks Articles:

Coin Change Problem (Dynamic Programming)
Greedy Algorithm for Minimum Coins
YouTube Tutorials:

Dynamic Programming - Coin Change Problem
Testing Your Code
To test your implementation:

Create a 0-main.py file as shown above.
Run the file in your terminal:
bash
Copy code
python3 0-main.py
Verify the output matches the expected results.

