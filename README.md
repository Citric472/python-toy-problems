# python-toy-problems

This repository contains solutions to three coding challenges implemented in Python. Each challenge is solved using a class-based approach for modularity and readability.

# Challenge 1: Minimum Moves to Equalize Boxes
File: challenge_one.py

Problem Statement:
Given an array of integers representing the number of bricks in each box, the task is to find the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function returns -1.

Class Overview:
Class Name: BrickArrangement
Methods:
__init__(self, A): Initializes the class with the input array A.
moves_needed(self) -> int: Calculates the minimum number of moves needed to equalize the number of bricks in each box.
Example Usage:

A = [7, 15, 10, 8]
arrangement = BrickArrangement(A)
print(arrangement.moves_needed())  # Output: 7

# Challenge 2: Maximum Sum of Pairs with Equal Digit Sums
File: challenge_two.py

Problem Statement:
Given an array of integers, the task is to find the maximum sum of two numbers whose digits add up to an equal sum. If no such pair exists, the function returns -1.

Class Overview:
Class Name: MaxDigitSumPair
Methods:
__init__(self, A): Initializes the class with the input array A.
digit_sum(self, number) -> int: Calculates the sum of the digits for a given number.
find_max_sum_pair(self) -> int: Finds the maximum sum of two numbers with equal digit sums.
Example Usage:

A = [51, 71, 17, 42]
pair_finder = MaxDigitSumPair(A)
print(pair_finder.find_max_sum_pair())  # Output: 93
# Challenge 3: String Generation
File: challenge_three.py

Problem Statement:
Given an integer N, the task is to generate a string of length N containing as many different lowercase letters as possible, where each letter occurs an equal number of times.

Class Overview:
Class Name: StringGenerator
Methods:
__init__(self, N): Initializes the class with the input integer N.
generate_string(self) -> str: Generates the required string based on the value of N.
Example Usage:

generator = StringGenerator(5)
print(generator.generate_string())  # Output: "aabb"