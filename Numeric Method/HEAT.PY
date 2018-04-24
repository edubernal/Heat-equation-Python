#heat

import sys, time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


L=1
T=1
Nx=22
Nt=1000
x = np.linspace(0, L, Nx+1)    # mesh points in space
dx = L/Nx
ddx = dx**2
t = np.linspace(0, T, Nt+1)    # mesh points in time
dt = T/Nt
F = dt/ddx  #if F>1/2,the finite diference method leads to growing solutions,ie, do not converge
u   = np.zeros((Nt+1, Nx+1))           # matrix that fills all the configurations u(x_i,t_i)
          
# Set initial condition u(x,0) = I(x)
for i in range(0, Nx+1):
	u[0, i] = 1

for n in range(1, Nt+1):
    # Compute u at inner mesh points
    for i in range(1, Nx):
        u[n, i] = u[n-1,i] + F*(u[n-1, i-1] - 2*u[n-1, i] + u[n-1, i+1])

    # Insert boundary conditions
    u[n, 0] = 1; u[n, Nx]=4


X, T = np.meshgrid(x, t)
fig = plt.figure ( )
ax = Axes3D ( fig )
surf = ax.plot_surface ( X, T, u,cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
plt.xlabel ( 'x' )
plt.ylabel ( 't' )
plt.title ( 'T(x,t) , $T_{2}=4$' )
plt.savefig ( 'heat.png' )
plt.show ( )




    