import os
import numpy as np

num_files = 10
for i in range(num_files):
    mean = (0, 0)
    corr = np.random.normal(0.95, 0.1, 1).item()
    cov = [[1, corr], [corr, 1]]
    x = np.random.multivariate_normal(mean, cov, size=500)
    np.savetxt(os.path.join("data", f"{i+1}.csv"), x, delimiter=";")
