import matplotlib.pyplot as plt

data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [3, 6, 2, 6, 7]}
plt.plot('data_x', 'data_y', data = data_dict)

plt.xlabel('X-Axis', loc='right')
plt.ylabel('Y-Axis', loc='top')

plt.show()