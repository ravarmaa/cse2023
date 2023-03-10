import math
import scipy.integrate as spi
import numpy as np

import matplotlib.pyplot as plt

k_p = 10
k_d = 2

previous_sign = 0

mass = 1
g = 9.81
l = 10
max_torque = 5


def control_function(angle, angular_velocity, time):
    global k_p, k_d, previous_sign, mass, g, l, max_torque

    sign = 1 if angle >= 0 else -1

    angle = angle % math.pi

    if sign == -1:
        angle = -math.pi + angle

    rate_sign = 1 if angular_velocity >= 0 else -1

    target_angle = sign*math.pi


    error = target_angle - angle

    error_derivative = -angular_velocity
    control_signal = k_p * error + k_d * error_derivative
    control_signal = max(min(control_signal, max_torque), -max_torque)

    # flip = rate_sign != previous_sign

    return abs(control_signal) * rate_sign
