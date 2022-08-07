from tkinter import font
import matplotlib.pyplot as plt

data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [3, 6, 2, 6, 7]}
plt.plot('data_x', 'data_y', data = data_dict)

# setting font
font1 = {
    'family' : 'monospace',
    'color' : 'deeppink',
    'weight' : 'bold',
    'size' : 14
}

font2 = {
    'family' : 'serif',
    'color' : 'deeppink',
    'weight' : 'normal',
    'size' : 'xx-large'
}

plt.xlabel('X-Axis', loc='right',labelpad=15, fontdict=font1)
plt.ylabel('Y-Axis', loc='top',labelpad=15, fontdict=font2)

plt.show()