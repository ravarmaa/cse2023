# for problem
# 3 putting a pole to -0.01 and zero to -0.285 (or also pole to -0.001 and
# zero to -0.0285, or you can go more insane if you want, but if you need
# to do this in real life with electronics components, for example, then
# it starts becoming impractical due to the component values you need to
# implement a corresponding circuit).

import control as ct
import matplotlib.pyplot as plt
import numpy as np

G = ct.tf([8, 15, 2], [7, 1, 3])

k = 1

pole = -0.001
zero = pole * 28.5

C = ct.zpk([zero], [pole], k)

F = C * G
ct.sisotool(ct.feedback(F))

plt.show()

# y, t = ct.step_response(ct.feedback(G))
# plt.plot(y, t)
# plt.show()
