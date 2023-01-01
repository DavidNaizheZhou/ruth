import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


def generate_data(num_files=10):

    # loop num_files times
    for i in range(num_files):

        # mean tuple
        mean = (0, 0)

        # correlation coefficient random distribution
        corr = np.random.normal(0.95, 0.1, 1).item()

        # covariance matrix
        cov = [[1, corr], [corr, 1]]

        # generate bivariate random variable
        x = np.random.multivariate_normal(mean, cov, size=500)

        # save to csv file
        np.savetxt(os.path.join("data", f"{i+1}.csv"), x, delimiter=";")


def plot_data():
    # loop through all files in data
    for file in os.listdir("data"):

        print(f"File: {file}")

        # load Data from .csv
        data = np.genfromtxt(os.path.join("data", file), delimiter=";")

        # extract cols
        x = data[:, 0]
        y = data[:, 1]

        # fit 1D polynomial to data
        model = np.polyfit(x, y, 1)

        # generate prediction function with coeff.
        predict = np.poly1d(model)

        # calculate R² Score
        r2 = r2_score(y, predict(x))

        # check and set color
        if r2 >= 0.9:
            color = "green"
        else:
            color = "red"

        # min, max for range
        min, max = np.min(x), np.max(x)

        ## plotting
        fig, ax = plt.subplots()

        # loaded data
        ax.scatter(x, y, s=4, c="black")

        # xpoints for regression line
        x_plot = np.linspace(min, max, 100)

        # plot regression line
        ax.plot(x_plot, predict(x_plot), c=color, label=f"y = {model[0]:.3f} x + {model[1]:.3f}\nR²={r2:.3f}")

        # plotting options
        ax.legend()
        ax.grid()
        ax.set_axisbelow(True)

        # save the figures to the folder plots
        plt.savefig(os.path.join("plots", f"{file.replace('.csv', '')}.png"))


if __name__ == "__main__":

    # generate_data(num_files=10)

    plot_data()
