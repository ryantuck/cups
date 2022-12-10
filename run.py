import json
import math

g = 10

def o_theta(theta_i, t):
    # radial downward motion from wi=0 due to gravity
    return theta_i - 1.0 * pow(t,2)

def w_omega(omega_i, t):
    # decay due to friction
    return omega_i * pow(math.e, 0 - 1.0 * t)

def v_c(rc, omega):
    return rc * omega

def ds(vc, dt):
    return vc * dt

def r_arc(v, theta):
    return 1/g * pow(v, 2) / (math.sin(theta)*math.cos(theta))

def da(ds, r):
    return ds / r

def move(x_i, y_i, phi_i, r, d_a):
    angle = (phi_i - math.pi / 2) % 2*math.pi
    x_f = x_i + math.cos(angle) * r
    y_f = y_i + math.sin(angle) * r
    phi_f = (phi_i + d_a) % 2*math.pi
    return x_f, y_f, phi_f


def simulate():

    n_steps = 1000
    dt = 0.01
    theta_min = math.pi / 4

    t = 0
    x, y = 0,0
    theta_i = 1.5
    rc = 2
    omega_i = 10
    v_i = v_c(rc, omega_i)
    v = v_i
    phi = math.pi / 2
    theta = theta_i


    for i in range(n_steps):

        print(json.dumps({'t': t, 'v': v, 'theta': theta, 'x': x, 'y': y, 'phi': phi}))

        if theta < theta_min:
            break

        r = r_arc(v, theta)
        d_s = ds(v, dt)
        d_a = da(d_s, r)

        x, y, phi = move(x, y, phi, r, d_a)

        t += dt
        theta = o_theta(theta_i, t)
        omega = w_omega(omega_i, t)
        v = v_c(rc, omega)




simulate()








