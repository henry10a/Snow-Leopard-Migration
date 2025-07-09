import numpy as np
import pandas as pd

def geometric_brownian_motion(S0, mu, sigma, T, dt=1):
    """Simulates GBM for snow leopard sightings over time"""
    N = int(T / dt)
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W) * np.sqrt(dt)  # Brownian motion
    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S0 * np.exp(X)
    return S
