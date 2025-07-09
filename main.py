import pandas as pd
from stochastic_utils import geometric_brownian_motion
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])

# Aggregate sightings by region
grouped = df.groupby("region")["sightings"].mean().reset_index()

print("📊 Average sightings per region:")
print(grouped)

# Predict frequency for each region using stochastic simulation
T = 12  # Predict 12 months ahead
mu = 0.05
sigma = 0.2

predictions = {}

for _, row in grouped.iterrows():
    region = row["region"]
    S0 = row["sightings"]
    sim = geometric_brownian_motion(S0, mu, sigma, T)
    predictions[region] = sim

# Plot one example
import random
example_region = random.choice(list(predictions.keys()))
plt.plot(predictions[example_region])
plt.title(f"Stochastic prediction for {example_region}")
plt.xlabel("Months Ahead")
plt.ylabel("Predicted Sightings")
plt.grid(True)
plt.show()
