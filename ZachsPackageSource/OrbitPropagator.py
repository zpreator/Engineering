import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

from ZachsPackage import PlanetaryData as pd

class OrbitPropagator:
    def __init__(self, r0, v0, tspan, dt, cb = pd.earth):
        """ r0 = initial """
        self.r0 = r0
        self.v0 = v0
        self.tspan = tspan
        self.dt = dt
        self.cb = cb

    def propagateOrbit(self):
        self.n_steps = int(np.ceil(self.tspan/self.dt))

        # initialize arrays
        self.ts = np.zeros((self.n_steps, 1))
        self.ys = np.zeros((self.n_steps, 6))

        # initial conditions
        self.y0 = self.r0 + self.v0
        self.ts[0] = 0
        self.ys[0] = self.y0
        self.step = 1

        self.solver = ode(self.diffy_q)
        self.solver.set_integrator('lsoda')
        self.solver.set_initial_value(self.y0, 0)
        

        # propagate orbit
        while self.solver.successful() and self.step<self.n_steps:
            t = self.solver.t
            self.solver.integrate(t+self.dt)
            self.ts[self.step] = self.solver.t
            self.ys[self.step] = self.solver.y
            self.step += 1

        self.rs = self.ys[:, :3]
        self.vs = self.ys[:,3:]

    def diffy_q(self, t, y):
        # Unpack state
        rx, ry, rz, vx, vy, vz = y
        r = np.array([rx, ry, rz])

        # norm of the radius vecotr
        norm_r = np.linalg.norm(r)

        # two body acceleration
        ax, ay, az = -r*self.cb['mu']/norm_r**3

        return [vx, vy, vz, ax, ay, az]

    def plot_3d(self, show_plot=False, save_plot=False, plotTitle=''):
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_subplot(111, projection='3d')

        

        # plot central body
        _u, _v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        _x = self.cb['radius']*np.cos(_u)*np.sin(_v)
        _y = self.cb['radius']*np.sin(_u)*np.sin(_v)
        _z = self.cb['radius']*np.cos(_v)
        ax.plot_surface(_x, _y, _z, cmap='Blues')

        ax.plot(self.rs[:,0], self.rs[:,1], self.rs[:, 2], 'w', label='Trajectory')
        ax.plot([self.rs[0, 0]], [self.rs[0, 1]], [self.rs[0, 2]], 'wo', label='Initial Position')

        # plot the x, y, z vectors
        l = self.cb['radius']*2
        x, y, z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        u, v, w = [[l, 0, 0], [0, l, 0], [0, 0, l]]

        ax.quiver(x, y, z, u, v, w, color='k')

        max_val = np.max(np.abs(self.rs))

        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])

        ax.set_xlabel(['X (km)'])
        ax.set_ylabel(['Y (km)'])
        ax.set_zlabel(['Z (km)'])

        ax.set_aspect('auto')

        ax.set_title(plotTitle)

        plt.legend()
        if save_plot:
            plt.savefig(plotTitle + '.png', dpi=300)
        if show_plot:
            plt.show()

r_mag = pd.earth['radius'] + 500.0
v_mag = np.sqrt(pd.earth['mu']/r_mag)

# initial position and velocity vectors
r0 = [r_mag, r_mag*0.01, r_mag*-0.1]
v0 = [0, v_mag, v_mag*0.3]

# 1 day
tspan = 100*60.0

# 100 seconds
dt = 100.0


op = OrbitPropagator(r0, v0, tspan, dt)
op.propagateOrbit()
op.plot_3d(show_plot=True)