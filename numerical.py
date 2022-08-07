import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,1000)
y_1 = np.sin(2 * x * np.pi)
y_2 = np.cos(2 * x * np.pi)
y_3 = np.ceil(3 * x)

fig , ax = plt.subplots()

ax.plot(x,y_1,'--') # 선 스타일을 쉽게 정할 수 있음.
ax.plot(x,y_2,'-.')
ax.plot(x,y_3, alpha = 0.7) # alpha : 선의 투명도

ax.spines['left'].set_position('center')
ax.spines['right'].set_visible('False')
ax.spines['top'].set_visible('False')
ax.spines['bottom'].set_position(('data',0))  
ax.tick_params('both', length = 0)



plt.show()