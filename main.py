import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# plt.plot([0,1,2,3,4])
# plt.ylabel('Numbers')
# plt.xlabel('x axis')
# plt.title("ploting x an y")

x = np.linspace(0,2,100)
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")

plt.ylabel('y axis')
plt.xlabel('x axis')

plt.title('simple plot')
plt.legend()

plt.show()

