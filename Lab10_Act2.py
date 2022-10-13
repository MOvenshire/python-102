# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# The team members listed below have actively contributed to this assignment.
#
# Name:         Victor Malbrel
#               Marissa Ovenshire
#               Rachel Bode
#               Matthew Ensmann
# Section:      ENGR 102-220
# Team:         Team 15
# Assignment:   Lab 10 Activity 2
# Date:         10/27/2020
#

import matplotlib.pyplot as plt
import numpy as np

FIGURE1=1
FIGURE2=2
FIGURE3=3

# Plot 1
x = np.linspace(-10, 10, 100)
f = 2
plt.plot(x, (1/( 4 * f))*x**2, linewidth=2.0, color='g')

f = 6
figure1=plt.figure(FIGURE1)
plt.plot(x, (1/( 4 * f))*x**2, linewidth=4.0, color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Parabola Plot with Varying Focal Point")
plt.legend(('line1', 'line2'))

# Plot 2
𝐴 = 2
𝐵 = 3
𝐶 = -11
𝐷 = -6
x = np.linspace( -4, 4, 25 )

figure2=plt.figure(FIGURE2)
plt.scatter(x, 𝐴*𝑥**3 + 𝐵*𝑥**2 + 𝐶*𝑥 + D , color="b", s=10)
plt.title("Plot of a Cubic Polynomial")
plt.xlabel("x values")
plt.ylabel("y values")

# Plot 3
x = np.linspace(-2*np.pi, 2*np.pi)

figure3=plt.figure(FIGURE3)
plt.plot(x, np.sin(x), 'b-')
plt.plot(x, np.cos(x), 'r-')
plt.title('Plot of cos(x) and sin(x)')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(('sin(x)', 'cos(x)'))
plt.show()
