import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 6, 8])
Y = np.array([3, 8, 1, 10])
plt.subplot(2,1,1)
plt.plot(X, Y)

plt.subplot(2,1,2)
plt.scatter(X, Y, c = np.arange(0,4), cmap = 'plasma', 
                s = [20, 50, 100, 500], alpha = 0.5)
plt.colorbar()

plt.show()

plt.subplot(2,3,1)
plt.bar(X, Y, width = 0.2)

plt.subplot(2,3,2)
plt.hist(X)

plt.subplot(2,3,3)
plt.pie(X, labels=["math","english","spain","physic"],
            explode = [0, 0, 0.2, 0], shadow = True)
plt.legend(title = "Score")

plt.subplot(2,3,5)
plt.plot(X, Y, marker = '*', ms = 20, mec = 'r', mfc = '#4CAF50',
                linestyle = 'dashed', lw = '20', c = 'y', )
plt.subplot(2,3,6)
plt.plot(X, Y, 'o:r')
plt.title('y = f(x)', {'color':'blue', 'size':20}, loc = 'left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis = 'x')

plt.suptitle("GRAPH")
plt.show()

fig = plt.figure()

np.random.seed(7)   #fix trạng thái random
x = np.linspace(0, 1, 100)
y = np.random.rand(100)
z = np.add(x, y)
ax = fig.add_subplot(1,3,1, projection = '3d')
ax.scatter(x, y, z)

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
#X = np.linspace(-1, 1, 100)
#Y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(1 - X**2 - Y**2)
ax = fig.add_subplot(1,3,2, projection = '3d')
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, -Z)

u = np.linspace(0, 2 * np.pi, 10)
v = np.linspace(0, np.pi, 10)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax = fig.add_subplot(1,3,3, projection = '3d')
ax.plot_surface(x, y, z)

plt.show()
