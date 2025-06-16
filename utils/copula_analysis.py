import numpy as np
import matplotlib.pyplot as plt
from copulas.bivariate import Clayton, Frank, Gaussian, Gumbel
from sklearn.preprocessing import QuantileTransformer

def fit_copula(x, y, copula_type='Gaussian'):
    data = np.vstack((x, y)).T
    qt = QuantileTransformer(output_distribution='uniform')
    u = qt.fit_transform(data)
    u1, u2 = u[:, 0], u[:, 1]

    copulas = {
        'Gaussian': Gaussian(),
        'Clayton': Clayton(),
        'Frank': Frank(),
        'Gumbel': Gumbel()
    }

    copula = copulas[copula_type]
    copula.fit(np.column_stack((u1, u2)))
    return copula, u1, u2

def plot_copula_density(copula, u1, u2, title="Copula Density"):
    grid = np.linspace(0.01, 0.99, 50)
    X, Y = np.meshgrid(grid, grid)
    Z = np.vectorize(lambda x, y: copula.probability_density([x, y]))(X, Y)

    fig, ax = plt.subplots(figsize=(6, 5))
    cp = ax.contourf(X, Y, Z, levels=15, cmap='viridis')
    fig.colorbar(cp)
    ax.set_title(title)
    ax.set_xlabel('U1')
    ax.set_ylabel('U2')
    return fig
 
