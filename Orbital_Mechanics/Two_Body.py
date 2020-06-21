import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('dark_background')

def plot(rs):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')

    

    # plot central body
    _u, _v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    _x = earth_radius*np.cos(_u)*np.sin(_v)
    _y = earth_radius*np.sin(_u)*np.sin(_v)
    _z = earth_radius*np.cos(_v)
    ax.plot_surface(_x, _y, _z, cmap='Blues')

    ax.plot(rs[:,0], rs[:,1], rs[:, 2], 'w', label='Trajectory')
    ax.plot([rs[0, 0]], [rs[0, 1]], [rs[0, 2]], 'wo', label='Initial Position')

    # plot the x, y, z vectors
    l = earth_radius*2
    x, y, z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    u, v, w = [[l, 0, 0], [0, l, 0], [0, 0, l]]

    ax.quiver(x, y, z, u, v, w, color='k')

    max_val = np.max(np.abs(rs))

    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    ax.set_xlabel(['X (km)'])
    ax.set_ylabel(['Y (km)'])
    ax.set_zlabel(['Z (km)'])

    ax.set_aspect('auto')

    ax.set_title('Orbiting stuff')

    plt.legend()

    plt.show()

earth_radius = 6378.0 # km
earth_mu = 398600.0 # km^3/s^2



def diffy_q(t, y, mu):
    # Unpack state
    rx, ry, rz, vx, vy, vz = y
    r = np.array([rx, ry, rz])

    # norm of the radius vecotr
    norm_r = np.linalg.norm(r)

    # two body acceleration
    ax, ay, az = -r*mu/norm_r**3

    return [vx, vy, vz, ax, ay, az]

if __name__ == '__main__':
    r_mag = earth_radius+500 # km
    v_mag = np.sqrt(earth_mu/r_mag)

    #initial position and velocity vectors
    r0 = [r_mag, 0, 0]
    v0 = [0, v_mag, 0]

    # Timespan
    tspan = 100 * 60.0

    # timestep
    dt = 100.0

    # total num steps
    n_steps = int(np.ceil(tspan/dt))

    # initialize arrays
    ys = np.zeros((n_steps, 6))
    ts = np.zeros((n_steps, 1))

    # initial conditions
    y0 = r0 + v0
    ys[0] = np.array(y0)
    step = 1

    solver = ode(diffy_q)
    solver.set_integrator('lsoda')
    solver.set_initial_value(y0, 0)
    solver.set_f_params(earth_mu)

    # propagate orbit
    while solver.successful() and step<n_steps:
        t = solver.t
        solver.integrate(t+dt)
        ts[step] = solver.t
        ys[step] = solver.y
        step += 1

    rs = ys[:, :3]

    plot(rs)