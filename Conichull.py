#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:54:11 2023

@author: shashankramachandran
"""
import numpy as np
import matplotlib.pyplot as plt



A = np.array([[1/5, 4/5],
              [4/5, 1/5]])

# Generate values for lambda1 and lambda2
lambda1 = np.linspace(0, 1, 10)
lambda2 = np.linspace(0, 1, 10)

# Generate generative points
generative_points = []
for l1 in lambda1:
    for l2 in lambda2:
        generative_points.append(l1 * A[:, 0] + l2 * A[:, 1])

generative_points = np.array(generative_points)

# Print the generative points
print("Generative Points:")
print(generative_points)


