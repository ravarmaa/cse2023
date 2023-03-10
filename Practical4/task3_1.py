import matplotlib.pyplot as plt
import control as ct

s = ct.tf('s')
# overdamped
H0 = 1/((s + 3)*(s + 2))
sys0 = ct.TransferFunction(H0)
# H1 = 1/(s+1)
# sys1 = ct.TransferFunction(H1)
# H2 = 1/(s+2)
# sys2 = ct.TransferFunction(H2)
# H3 = 1/(s+3)
# sys3 = ct.TransferFunction(H3)

# Plot step response of both transfer functions
t, y0 = ct.step_response(sys0)
# t, y1 = ct.step_response(sys1)
# t, y2 = ct.step_response(sys2)
# t, y3 = ct.step_response(sys3)
plt.plot(t, y0, label='Pole at -2 -3')

# plt.plot(t, y1, label='Pole at -1')
# plt.plot(t, y2, label='Pole at -2')
# plt.plot(t, y3, label='Pole at -3')
# plt.legend()
plt.show()



ct.pzmap(sys0, plot=True)
plt.show()