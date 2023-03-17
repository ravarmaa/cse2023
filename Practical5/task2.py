import control as ct
import matplotlib.pyplot as plt
import numpy as np
# cz = 0.1
# cp = 1

#C = (s + cz) / (s + cp)

# For problem 2 putting a pole to -7 and zero to -5 works, and
G = ct.zpk([], [3, -2], 1)
# Remember: Gain 0 puts them at poles, gain infinity puts them at zeros
k = 100

zero = -5
pole = -7

C = ct.zpk([zero], [pole], k)

F = C * G
ct.sisotool(F)

plt.show()
