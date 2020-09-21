import matplotlib.pyplot as plt
import numpy as np
import os


fig, ax = plt.subplots()
x = np.linspace(-10, 10, num = 401)
A = 1.34941
y = -0.0001*(np.fabs(np.sin(x)*np.sin(A)*np.exp(np.fabs(100-((x**2 + A**2)**0.5)/np.pi)))+1)**0.1
path = 'results'
if not os.path.exists(path):
    os.mkdir(path)#Создаю папку
file = open(r'results\task_01_207_VOLKOVSKIY_6.txt','w')
count = 0
while count < x.size:
    file.write(str(x[count]))
    file.write("    ")
    file.write(str(y[count]))
    file.write("\n")
    count += 1
file.close()
ax.plot(x, y)
plt.show()
