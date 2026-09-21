import numpy as np
import joblib
from pathlib import Path
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Dummy dataset (2 features)
X = np.array([[1, 100], [2, 200], [3, 300], [4, 400], [5, 500]], dtype=float)
y = np.array([10, 20, 30, 40, 50], dtype=float)

# Train multiple models
lr = LinearRegression().fit(X, y)
rf = RandomForestRegressor(random_state=42).fit(X, y)

# Compare (R^2 on training set for simplicity)
lr_score = lr.score(X, y)
rf_score = rf.score(X, y)

print("LinearRegression R2:", lr_score)
print("RandomForest R2:", rf_score)

# Choose best
best_model = rf if rf_score >= lr_score else lr

# Save model
Path("models").mkdir(exist_ok=True)
joblib.dump(best_model, "models/model.pkl")
print("Saved best model to models/model.pkl")

# Save a simple comparison plot
Path("notebooks").mkdir(exist_ok=True)
models = ["LinearRegression", "RandomForest"]
scores = [lr_score, rf_score]
plt.figure()
plt.bar(models, scores)
plt.title("Model Comparison (R2)")
plt.xlabel("Model")
plt.ylabel("Score")
plt.savefig("notebooks/model_comparison.png")
print("Saved model comparison plot to notebooks/model_comparison.png")
