import numpy as np
import matplotlib.pyplot as plt
def initialBell(x):
    return np.where(x%1.<0.5, np.power(np.sin(2*x*np.pi), 2), 0)

def main():
    nx=40
    c=0.2
    x=np.linspace (0.0, 1.0, nx+1)
    phi = initialBell(x)
    phiNew = phi.copy()
    phiOld = phi.copy()

    for j in range(1, nx):
        phi[j]= phiOld[j] - 0.5*c*(phiOld[j+1]-phiOld[nx-1])
    phi[0] = phiOld[0] - 0.5*c*(phiOld[1]-phiOld[nx-1])
    phi[nx] = phi [0]

    nt = 40
    for n in range(1, nt):
        for j in range (1, nx):
            phiNew[j] = phiOld[j] - c*(phi[j+1]-phi[j-1])
        phiNew[0] = phiOld[0] - c*(phi[1]-phi[nx-1])
        phiNew[nx]=phiNew[0]

        phiOld = phi.copy()
        phi = phiNew.copy()

    u=1.
    dx = 1./nx
    dt = c*dx/u
    t = nt*dt

    plt.plot (x, initialBell (x - u*t), 'k', label='analytic')
    plt.plot(x, phi, 'b', label='CTCS')
    plt.legend(loc='best')
    plt.ylabel('$\phi$')
    plt.axhline(0, linestyle=':' , color='black')
    plt.show()
    
main()

