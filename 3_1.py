import matplotlib.pyplot as plt
x = list(range(0, 2000))
y = []
for i in x:
    y.append(i**2)
plt.plot(x, y)
plt.show()