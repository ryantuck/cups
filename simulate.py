import json
import math


def is_finished(state):
    return False

def _iterate_time(t, dt):
    return round(t + dt, 1)

def _iterate_velocity(v):
    v['speed'] = v['speed'] * 0.9
    return v


def _linear_motion(pos, v, dt):
    angle = v['angle']
    speed = v['speed']
    x = pos['x']
    y = pos['y']

    distance = speed / dt

    x_f = x + distance * math.cos(angle)
    y_f = y + distance * math.sin(angle)

    return {'x': x_f, 'y': y_f}


def _iterate_position(pos, v, dt):
    return _linear_motion(pos, v, dt)


def iterate(state):
    dt = 0.1
    state['t'] = _iterate_time(state['t'], dt)
    state['v'] = _iterate_velocity(state['v'])
    state['pos'] = _iterate_position(state['pos'], state['v'], dt)
    return state

def simulate():

    state = {'t': 0, 'v': {'speed': 8, 'angle': math.pi/4}, 'pos': {'x': 0, 'y': 0}}
    n_steps = 100

    for i in range(n_steps):
        if is_finished(state):
            break
        state = iterate(state)
        print(json.dumps(state))

simulate()
