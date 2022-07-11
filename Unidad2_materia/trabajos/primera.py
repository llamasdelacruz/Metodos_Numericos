import numpy as np
import matplotlib.pyplot as plt
f = lambda x:(np.sin(10*x) + np.cos(3*x))
#f = lambda x:(np.sin(20*x)+3)
x = np.linspace(-2,5)
ox = 0*x
plt.plot(x, ox, "-k")
plt.plot(x, f(x))

plt.show()

print(f(-2))
print(f(5))
