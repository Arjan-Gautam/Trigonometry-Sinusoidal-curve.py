import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, np.pi * 2, 100)
y = np.sin(x)
plt.plot(x, y, label='y = sin(x)' ,color= 'purple') 
plt.title("Sinusoidal curve")
plt.xlabel("x (in degree)")
plt.ylabel("sin(x)")
plt.legend() 
plt.grid(True)
xticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
xtick_labels = ['0', '90', '180', '270', '360']
plt.xticks(xticks, xtick_labels) 
plt.show()
