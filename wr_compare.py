#!/usr/bin/env python3

"""
This program determines the accuracy of the various methods of weighted residuals by comparing it with the analytical solution. In this program, we consider the differential equation u" + u = 1 (BCs: u(0) = 1 and u(1) = 0) and solve it using collocation, subdomain, least squares, Petrov-Galerkin methods. 

Assume a 2 term approximation, and define u(x) = a0 + a1 * x + a2 * x^2. Upon applying the boundary conditions, we get a0 = 1 and a1 = -(1 + a2) resulting in only one unknown: a2. The residual is obtained as R(x) = -x + a2 * (x^2 - x + 2).

This program is based on a class I am taking: ME311 - Finite Element Methods.
"""

import numpy as np 
import matplotlib.pyplot as plt 

# Initializing the domain

L = 1 						# The system length 
N = 101 					# Number of discretizations
x = np.linspace(0, L, N)   	# Domain initialized as a 1-D array

# Exact solution
y_anal = 1 - np.sin(x)/np.sin(np.degrees(1))

# Solutions by weighted residuals methods

y_coll = 1 - x + 2/7 * (x**2 - x) 		# Solved by collocation method, assuming residual is 0 at x = 0.5
y_subd = 1 - x + 3/11 * (x**2 - x) 		# Solved by subdomain method, assuming only 1 subdomain to find a2, and w = 1
y_lsqr = 1 - x + 165/606 * (x**2 - x) 	# Solved by least squares method, where the weight function = dR/d(a2)
y_pgal = 1 - x + 5/18 * (x**2 - x) 		# Solved by Petrov-Galerkin method, assuming the weight function = du/d(a2)

# Plotting the solutions

num_plots = 5 			# Number of plots in the figure
colormap = plt.cm.jet
plt.gca().set_prop_cycle(plt.cycler('color', colormap(np.linspace(0, 1, num_plots))))

plt.plot(x, y_anal, label = "Analytical solution")
plt.plot(x, y_coll, label = "Collocative at x = 0.5", linewidth = 5, alpha = 0.5)
plt.plot(x, y_subd, label = "Subdomain with w = 1", linewidth = 4, linestyle = "dashed", alpha = 0.5)
plt.plot(x, y_lsqr, label = "Least Squares")
plt.plot(x, y_pgal, label = "Petrov-Galerkin with w = du/da2", linestyle = '-.')
plt.legend()
plt.savefig("wr_compare.png")