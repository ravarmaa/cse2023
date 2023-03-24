import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Problem 1

# Initial conditions, 10000 people, 10 infected
z0 = np.array([[10000],  # Not infected z1_dot
               [10],  # Infected z2_dot
               [0],  # Immune z3_dot
               [0]])  # Dead z4_dot

a = 1 / 100  # healthy -> dead
b = 10 / 100  # healthy -> infected
c = 1 / 100  # healthy -> immune
d = 50 / 100  # infected -> dead
e = 25 / 100  # infected -> immune
f = 1 / 100  # immune -> dead

u = np.array([[10,  # new healthy
              10]])  # new infected

# z1_dot = -a*z1 - b*z1 - c*z1 + u1  - healthy people change
# z2_dot = b*z1 - d*z2 - e*z2 + u2 - infected people change
# z3_dot = c*z1 + e*z2 - f*z3 - immune people change
# z4_dot = a*z1 + d*z2 + f*z3 - dead people change

A = np.array([[-a - b - c, 0, 0, 0],
              [b, -d - e, 0, 0],
              [c, e, -f, 0],
              [a, d, f, 0]])

B = np.array([[1, 0],
              [0, 1],
              [0, 0],
              [0, 0]])

C = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0]])

D = np.array([[0, 0],
              [0, 0],
              [0, 0]])

sys = ct.ss(A, B, C, D)

# Plottery
no_of_days = 200
days = np.linspace(0, no_of_days, no_of_days + 1)

time, outputs = ct.initial_response(sys, T=days, X0=z0)
print(outputs)


fig, (ax1, ax2) = plt.subplots(1, 2)

total_people = outputs[0] + outputs[1] + outputs[2]

ax1.set_title("Initial response")
ax1.plot(time, outputs[0], label="Uninfected")
ax1.plot(time, outputs[1], label="Infected")
ax1.plot(time, outputs[2], label="Immune")
ax1.plot(time, total_people, label="Population")
ax1.legend()

# Putting u in
u = np.tile(u, (len(days), 1))
u = np.transpose(u)

time, outputs = ct.forced_response(sys, T=days, U=u, X0=z0)

total_people = outputs[0] + outputs[1] + outputs[2]
ax2.set_title("Forced response")
ax2.plot(time, outputs[0], label="Uninfected")
ax2.plot(time, outputs[1], label="Infected")
ax2.plot(time, outputs[2], label="Immune")
ax2.plot(time, total_people, label="Population")
ax2.legend()
plt.show()

# Problem 2
z0 = np.array([[0],
               [0],
               [0]])

R = 1000
C1 = 10e-9
C2 = 100e-9
L = 0.1

A = np.array([[-1 / (R * C1), 0, -1 / C1],
              [0, 0, 1 / C2],
              [1 / L, -1 / L, 0]])

B = np.array([[1 / (R * C1)],
              [0],
              [0]])

C = np.array([[1, 0, 0],
              [0, 1, 0],
              [1, -1, 0]])

D = 0

sys = ct.ss(A, B, C, D)
time, outputs = ct.step_response(sys)
print(outputs)
plt.plot(time, outputs[0][0], label="v1")
plt.plot(time, outputs[1][0], label="v2")
plt.plot(time, outputs[2][0], label="v3")
plt.legend()
plt.show()
