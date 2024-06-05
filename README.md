# Tetrahedron

This challenge is designed to assess your problem-solving and programming skills. Please read the instructions carefully before you begin.


## Instructions:

    Your task is to write a program that processes these files to solve the given problem.
    The results should be submitted in the specified format.

## Problem Description:

You are to write a program that reads a list of points on a 3D plane from a file. Each point is defined by its coordinates and an associated number and is presented in the following format: (x, y, z, n), where x, y, and z are floats, and n is an integer ranging from 0 to 100

## Your task: 

Identify the indices of four points that form a 'valid' tetrahedron with the smallest possible volume.

A'valid' tetrahedron has to be formed with points such that the sum of their n values is equal to 100


### Example:

Suppose you the following points:

(3.00, 4.00, 5.00, 22)
(2.00, 3.00, 3.00, 3)
(1.00, 2.00, 2.00, 4)
(3.50, 4.50, 5.50, 14)
(2.50, 3.50, 3.50, 24)
(6.70, 32.20, 93.0, 5)
(2.50, 3.00, 7.00, 40)

A tetrahedron formed by the points with indices 0, 3, 4, 6 is the only valid tetrahedron in this example; because 22 + 14 + 24 + 40 = 100

The output should list the zero-based indices of these four points in ascending order.


## Results:
Your code should return a list of four points that form the smallest tetrahedron for each input file.

    You should return the indexes in ascending order.
    Make sure that the indexes start at 0.