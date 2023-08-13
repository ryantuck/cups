import json
import math

from pydantic import BaseModel

class Velocity(BaseModel):
    angle: float
    speed: float

class Position(BaseModel):
    x: float
    y: float

class State(BaseModel):
    time: float
    position: Position
    velocity: Velocity

def is_finished(state):
    return False

def _iterate_time(t, dt):
    return round(t + dt,  1)

def _iterate_speed(speed):
    return 0.9 * speed

def _iterate_angle(angle):
    return angle

def _iterate_velocity(v):
    v.speed = _iterate_speed(v.speed)
    v.angle = _iterate_angle(v.angle)
    return v

def _linear_motion(pos, v, dt):

    distance = v.speed / dt

    x_f = pos.x + distance * math.cos(v.angle)
    y_f = pos.y + distance * math.sin(v.angle)

    return Position(x=x_f, y=y_f)


def _iterate_position(pos, v, dt):
    return _linear_motion(pos, v, dt)


def iterate(state):

    dt = 0.1

    state.time = _iterate_time(state.time, dt)
    state.velocity = _iterate_velocity(state.velocity)
    state.position = _iterate_position(state.position, state.velocity, dt)

    return state

def simulate():

    state = State(
        time=0,
        position=Position(x=0,y=0),
        velocity=Velocity(speed=8, angle=math.pi/4),
    )
    n_steps = 100

    for i in range(n_steps):
        if is_finished(state):
            break
        state = iterate(state)
        print(json.dumps(state.dict()))

simulate()
