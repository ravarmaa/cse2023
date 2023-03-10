import control as ct
import matplotlib.pyplot as plt

# Define transfer functions

# undamped
s = ct.tf('s')
H0 = 1/(s**2 + 1)
sys0 = ct.TransferFunction(H0)

t, y0 = ct.step_response(sys0)
plt.plot(t, y0, label='Pole at +-j')
plt.legend()
plt.show()

ct.pzmap(sys0, plot=True)
plt.show()
