import numpy as np
import matplotlib.pyplot as plt

with open("/home/b01-101/Desktop/OIP/BatYa_PnG/8  - GRAPH/settings.txt", "r") as settings: # путь файла settings
    tmp = [float(i) for i in settings.read().split("\n")]

set_array = np.loadtxt("/home/b01-101/Desktop/OIP/BatYa_PnG/8  - GRAPH/settings.txt", dtype = float)
data_array = np.loadtxt("/home/b01-101/Desktop/OIP/BatYa_PnG/8  - GRAPH/data.txt", dtype = int)

fig, ax = plt.subplots(figsize = (16, 11), dpi = 200)


data_array = data_array * set_array[0]
y = data_array
x = [0] * 898

for i in range(898):
    x[i] = i * set_array[1]

t_charge = np.argmax(data_array) * set_array[1]

t_down = (898 - np.argmax(data_array)) * set_array[1]

plt.title("Процесс заряда и разряда конденсатора в RC - цепочке", color = 'blue')

ax.grid(color = "red",    #  цвет линий
        linewidth = 0.45,    #  толщина
        linestyle = 'dashed')

ax.minorticks_on()

ax.grid(which='minor',
        color = 'orange',
        linewidth = 0.25,
        linestyle = 'dashed')

plt.plot(x, y, '-b', label='Зависимость', markevery=70, marker = "s")

plt.legend()
ax.set_xlabel('Время t (с)')
ax.set_ylabel('Напряжение U (В)')
plt.text(6, 1.5, 'время зарядки %f' % t_charge, fontsize=10)
plt.text(6, 2, 'время разрядки %f' % t_down, fontsize=10)

print(t_charge)
print(t_down)

plt.xlim (0, 10)
plt.ylim (0, 3.5)

plt.text(0, 8, 'время зарядки %f' % t_charge, fontsize=500)


fig.savefig("png.svg")
plt.show()
