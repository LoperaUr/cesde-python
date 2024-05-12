import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]
keys = ["A", "B", "C", "D"]

## gráficos de pastel
pie = plt.pie(sizes, labels=keys)

plt.show()

