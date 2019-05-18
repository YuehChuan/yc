import numpy as np
import matplotlib.pyplot as plt

G= np.array([140,140,140,140,140,140,110,110,110,110,110,140,140,140,140,140,140])
#test case 
#G = np.array([1,1,2,2,2,1,1])

arraySize = G.size
print arraySize
G_plum = np.zeros(arraySize)
G_plum_plum= np.zeros(arraySize)


G_plum[0]=140
for i in range (1,arraySize-1):
        currentElement=G[i]
        left= G[i-1]
        right = G[i+1]
        total = currentElement +left +right
        avg = total/3.0
        G_plum[i] = avg 

G_plum[arraySize-1] = (G[arraySize-2]+G[arraySize-1]+140 )/3.0

print G
print G_plum 

G_plum_plum = 2*G - G_plum
print G_plum_plum

#plot 3 sequences in same picture
s = np.arange(0, 17, 1)
plt.plot(s,G, 'ro', s, G_plum, 'bo', s, G_plum_plum, 'k')

plt.show()
