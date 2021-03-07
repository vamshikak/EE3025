import numpy as np
import matplotlib.pyplot as plt

k = 30
x = np.array([1.0,2.0,1.0,4.0,3.0,3.0])
xl = len(x)
x = np.concatenate([x,np.zeros(k-xl)])
y = np.zeros(k)
#print(xl)
#print(len(x))
#print(len(y))

#according to system equation given	
y[0] = x[0]
y[1] = -0.5*y[0]+x[1]
for i in range(2,k-1):
	y[i] = -0.5*y[i-1]+x[i]+x[i-2]

#printing maximum elements
print("Upper bound of x(n) is", max(x))
print("Upper bound of y(n) is", max(y))

#plotting
fig, axs = plt.subplots(2)
#fig.suptitle('conv_xy')
axs[0].stem( x)
axs[0].grid()
axs[0].set_xlabel('n')
axs[0].set_ylabel('x(n)')
#axs[0].set_title('Input signal x(n)')
axs[1].stem(y)
axs[1].set_xlabel('n')
axs[1].set_ylabel('y(n)')
#axs[1].set_title('Output signal y(n)')
axs[1].grid()
plt.show()