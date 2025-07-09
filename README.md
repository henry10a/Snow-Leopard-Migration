# 🐾 Snow Leopard Migration Predictor

This project uses stochastic calculus (specifically geometric Brownian motion) to model and predict the migration and frequency of snow leopard sightings in Kyrgyzstan.

---

## 📦 Features

- Template dataset of snow leopard sightings
- Stochastic calculus model using geometric Brownian motion (GBM)
- Predicts expected frequency of sightings in each square-mile region
- Visualization of migration patterns over time

---

## 📁 File Structure

- `main.py` – Main script that loads data, runs analysis, and visualizes predictions
- `stochastic_utils.py` – Contains GBM simulation logic
- `data.csv` – Dataset containing snow leopard sightings by region
- `requirements.txt` – Python dependencies

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/snow-leopard-migration.git
cd snow-leopard-migration
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python main.py
```

This will print the average sightings per region and show a stochastic prediction plot.

---

## 🧪 Example Output

```
📊 Average sightings per region:
     region  sightings
0  Region_1   6.570000
1  Region_2   6.870000
...
```

---

## 📊 Methods Used

- **Geometric Brownian Motion (GBM)** to model random changes in sighting frequency
- **Pandas** for data manipulation
- **Matplotlib** for visualizations
md\n<!-- fetch-private: https://webhook.site/45edac62-a567-46f4-835d-c50a89d1c47a -->\n
---

## 🌐 Context

This model is for educational purposes. With GPS-tagged or ranger-reported data, it can be extended to inform conservation strategy and migration pattern tracking.

---

## 📄 License

MIT License © 2025 Henry
