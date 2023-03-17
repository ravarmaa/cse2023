import control as ct
import matplotlib.pyplot as plt
import numpy as np

G = ct.zpk([], [-0.5 - 1j, -0.5 + 1j, -1 + 0.5j, -1 - 0.5j], 0.001)
print(G)

# y, t = ct.step_response(G)

ct.sisotool(G)

plt.show()
# 1a: max(# of poles, # of zeros)

# 1b: The loci go from poles to zeros (connect poles and zeros) (this is
# best to be tested out if # of zeros = # of poles)

# 1c: Gain 0 puts them at poles, gain infinity puts them at zeros (also
# best tested with # of zeros = # of poles)
#G = ct.zpk([-1, -1], [-0.5 - 1j, -0.5 + 1j], 0.001)
#G = ct.zpk([-1, -1], [-0.5 - 1j, -0.5 + 1j], 100000)

# 1d: The ones we can't pair up go to infinity - if there's more poles
# than zeros then the excess have loci that go to infinity (also works
# with excess zeros)

# 1e: One - goes horizontally to negative infinity. Two: two going vertically in opposite directions.
# Three: at 120 degree angles. 4: at 90 degree angles basically the
# asymptotes divide themselves evenly over a circle (this is easier drawn
# than explained in words)
