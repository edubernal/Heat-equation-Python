#total production of entropy

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
F = dt/ddx  #if F>1/2,the finite diference method leads to growing solutions
u = np.zeros((Nt+1, Nx+1))           # matrix that fills all the configurations u(x_i,t_i)
          
# Set initial condition u(x,0) = I(x)
for i in range(0, Nx+1):
	u[0, i] = 1

for n in range(1, Nt+1):
    # Compute u at inner mesh points
    for i in range(1, Nx):
        u[n, i] = u[n-1,i] + F*(u[n-1, i-1] - 2*u[n-1, i] + u[n-1, i+1])

    # Insert boundary conditions
    u[n, 0] = 1; u[n, Nx]=10


e = np.zeros((Nt+1,Nx+1))
g = 1/ddx

for n in range(75,Nt+1): #compute the local production of entropy formula by taking discretes derivatives as we are doing so far in this project

	for i in range(1,Nx):
		e[n,i] = g*(1-2*(u[n,i+1]/u[n,i])+(u[n,i+1]/u[n,i])**2)

p = np.zeros((Nt+1,Nx+1)) 

for n in range(75,Nt+1): # in this step we taking the riemann definition of integral to calculate a discrete sum to perfom the integral of the local produdtion of entropy

	for i in range(1,Nx):
		p[n,i] = sum(e[n,m]*x[m] for m in range(1,Nx+1))




xx, tt = np.meshgrid(x, t)
fig= plt.figure ( )
ax = Axes3D ( fig )
surf = ax.plot_surface ( xx, tt, p,cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
plt.xlabel ( 'x')
plt.ylabel ( 't' )
plt.title ( 'P(x,t) , $T_{2}=10$'  )
plt.savefig ( 'Tentropy.png' )
plt.show()