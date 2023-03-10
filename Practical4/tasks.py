import control as ct
import matplotlib.pyplot as plt

# Task 1

# 3/1

# 5/(1*s + 0)

# (1*s+0)/1


sys1 = ct.tf(3, 1)
sys2 = ct.tf(5,[1,0])
sys3 = ct.tf([1,0],1)
sys4 = ct.parallel(sys1, sys2, sys3)
sys5 = ct.tf(3, [1,-5,6])
sys = ct.series(sys4,sys5)
sys = ct.feedback(sys, sign=-1)
# print(sys)

# alternatively

s = ct.tf('s')

G1 = 3
G2 = 5/s
G3 = s
G4 = 3/(s**2 - 5*s + 6)

sys = ct.feedback((G1+G2+G3)*G4)

print(sys)

# Task 2
poles = ct.poles(sys)
print(poles)

zeros = ct.zeros(sys)
print(zeros)

ct.pzmap(sys, plot=True)
plt.show()