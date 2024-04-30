%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import time

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

x = np.linspace(-5,5,100)
y = 2*x**2

plt.xlim(-5, 5)
plt.ylim(0, 50)

fig.show()
fig.canvas.draw()

for i in range(len(x)):
    ax.clear()
    ax.plot(x[:i], y[:i])
    fig.canvas.draw()
    # you can control the interval each point by setting the time for sleep
    time.sleep(0.5)    