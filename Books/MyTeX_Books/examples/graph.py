import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 5, 50)
y = x**2 + x + 1 + np.random.normal(0, 1, size=x.shape)

plt.scatter(x, y, color='blue', label='Данные')
plt.plot(x, 5*x + 1, color='red', label='Истинная прямая')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid(True)
plt.title('Линейная зависимость с шумом')
plt.savefig("../images/error_data.png", dpi=300, bbox_inches='tight')
plt.show()
