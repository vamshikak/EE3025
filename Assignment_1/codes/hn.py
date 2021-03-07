import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt


i=0.0

fig, axs = plt.subplots(1)
fig.suptitle('Region Of Convergence')
axs = plt.subplot(1,1,1)

plt.axvline(i,color='black') 
plt.axhline(i,color='black')
plt.axis('scaled')
plt.xlim([i-1.5, i+1.5])
plt.ylim([i-1.5, i+1.5])
plt.plot(0.0,1, marker = 'o', color='black') #markings zeros and poles
plt.plot(0.0,-1, marker = 'o', color='black') 
plt.plot(-0.5,0.0, marker = 'x', color='black') 
plt.plot(0.0,0.0, marker = 'x', color='black') 


axs.add_patch(patches.Circle((0,0), 1, fill=False,color='black')) #boundry for outer circle with r=1
axs.add_patch(patches.Circle((0,0), 0.5, fill=False, color='black'))  #boundry for inner circle with r=0.5
axs.add_patch(patches.Circle((0,0), 0.5,fill=True,color='white'))  #filling colour for inner circle with r=0.5

x = np.linspace(-1.5,1.5,1000)  
y1 = np.sqrt(16-x**2)
plt.fill_between(x,y1,-y1, color='y') 
plt.text(0.8,0.2,"|z|>0.5")  #values of zeros and poles
plt.text(0,-0.2,"z=0")
plt.text(-0.7,-0.2,"z=-0.5")
plt.text(0,1.1,"z=1j")
plt.text(0,-0.9,"z=-1j")

plt.grid()
plt.show()