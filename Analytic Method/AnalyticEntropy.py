#analitic entropy
 
import sys, time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

L=1
T=0.005
T1= 1
T2= 2
Nx= 100
Nt= 100
x = np.linspace(0, L, Nx+1)    # mesh points in space
dx = L/Nx
ddx = dx**2
t = np.linspace(0, T, Nt+1)    # mesh points in time
dt = T/Nt
u= np.zeros((Nt+1,Nx+1))





for i in range(0,Nt+1):
	                 
	for n in range(0,Nx+1):

		u[i,n]=T1+((T2-T1)/L)*x[n]+sum((((4*T1*(np.sqrt(2/L)))/(m*np.pi))*np.exp(-((m*np.pi/L)**2)*t[i])*np.sin((m*np.pi/L)*x[n])) for m in range(1,51,2))



e=np.zeros((Nt+1,Nx+1))

for i in range(0,Nt+1):

	for n in range(0,Nx+1):
		e[i,n]= (1/u[i,n])*(1+sum(((4*np.exp(-((m*np.pi/L)**2)*t[i])*np.cos((m*np.pi/L)*x[n])) for m in range(1,51,2))))


X, T = np.meshgrid(x, t)
fig = plt.figure ( )
ax = Axes3D ( fig )
surf = ax.plot_surface ( X, T, e)
plt.xlabel ( 'x' )
plt.ylabel ( 't' )
plt.title ( 'sigma(x,t)' )
plt.savefig ( 'entroanalytic.png' )
plt.show ( )