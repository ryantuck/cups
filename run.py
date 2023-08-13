import json
import math

g = 10
OMEGA_DECAY_RATE = 1 # speed
THETA_DECAY_RATE = 0.01 # fall angle

def o_theta(theta_i, t):
    # radial downward motion from wi=0 due to gravity
    return theta_i - THETA_DECAY_RATE * pow(t,2)

def w_omega(omega_i, t):
    # decay due to friction
    return omega_i * pow(math.e, 0 - OMEGA_DECAY_RATE * t)

def v_c(rc, omega):
    return rc * omega

def ds(vc, dt):
    return vc * dt

def r_arc(v, theta):
    return 1/g * pow(v, 2) / (math.sin(theta)*math.cos(theta))

def da(ds, r):
    return ds / r


def add_angles(angle, d_angle):
    angle_sum = (angle + d_angle + 2*math.pi) % (2*math.pi)

def move(x_i, y_i, phi_i, r, d_a):

    # get radial angle from tangent
    angle = (phi_i - (math.pi / 2) + 2*math.pi) % (2*math.pi)

    # find center of circle
    x_c = x_i + math.cos(angle) * r
    y_c = y_i + math.sin(angle) * r

    angle_2 = (angle - d_a - math.pi + 2*math.pi) % (2*math.pi)

    x_f = x_c + math.cos(angle_2) * r
    y_f = y_c + math.sin(angle_2) * r
    phi_f = (phi_i - d_a + 2*math.pi) % (2*math.pi)

    return x_f, y_f, phi_f


def simulate():

    n_steps = 100
    dt = 0.1
    theta_min = math.pi / 4

    t = 0
    x, y = 0,0
    theta_i = 1.5

    rc = 2

    omega_i = 40
    v_i = v_c(rc, omega_i)
    v = v_i
    #phi = math.pi / 2
    phi = 1.6
    theta = theta_i

    print(json.dumps({'t': t, 'v': v, 'theta': theta, 'x': x, 'y': y, 'phi': phi}))


    for i in range(n_steps):

        if theta < theta_min:
            break

        t += dt
        theta = o_theta(theta_i, t)
        omega = w_omega(omega_i, t)

        v = v_c(rc, omega)
        r = r_arc(v, theta)
        d_s = ds(v, dt)
        d_a = da(d_s, r)

        x, y, phi = move(x, y, phi, r, d_a)

        print(json.dumps({'t': t, 'v': v, 'theta': theta, 'x': x, 'y': y, 'phi': phi, 'r': r, 'ds': d_s, 'da': d_a}))


simulate()
