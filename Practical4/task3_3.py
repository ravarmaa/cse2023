import control as ct
import matplotlib.pyplot as plt
import numpy as np

# underdamped
K = 1.0 # gain
omega_n = 10.0 # natural frequency
zeta = 0.5 # damping ratio

# Define transfer function
num = [K * omega_n**2]
den = [1, 2*zeta*omega_n, omega_n**2]
sys = ct.TransferFunction(num, den)

# Calculate step response
t, y = ct.step_response(sys)

# Plot step response
plt.plot(t, y)
plt.xlabel('Time (seconds)')
plt.ylabel('Output')
plt.title('Step Response of Underdamped System')
plt.grid()
plt.show()


ct.pzmap(sys, plot=True)
plt.show()