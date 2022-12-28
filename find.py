import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

for file in os.listdir("data"):
    print(f"File: {file}")
    data = np.genfromtxt(os.path.join("data", file), delimiter=";")
    x = data[:, 0]
    y = data[:, 1]

    model = np.polyfit(x, y, 1)
    predict = np.poly1d(model)
    r2 = r2_score(y, predict(x))

    if r2 >= 0.9:
        color = "green"
    else:
        color = "red"

    min, max = np.min(x), np.max(x)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=4, c="black")
    x_plot = np.linspace(min, max, 100)
    ax.plot(x_plot, predict(x_plot), c=color, label=f"y = {model[0]:.3f} x + {model[1]:.3f}\nR²={r2:.3f}")
    ax.legend()
    ax.grid()
    ax.set_axisbelow(True)
    plt.savefig(os.path.join("plots", f"{file.replace('.csv', '')}.png"))
