import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv("data/lap_data.csv")

# Features and label
X = df[["compound", "tire_age"]]
y = df["lap_time"]

# Pipeline with OneHotEncoder for compound + linear model
preprocessor = ColumnTransformer([
    ("compound", OneHotEncoder(), ["compound"])
], remainder="passthrough")

model = Pipeline([
    ("pre", preprocessor),
    ("reg", LinearRegression())
])

model.fit(X, y)

# Save model
joblib.dump(model, "models/lap_time_predictor.pkl")
print("✅ Lap time model trained and saved.")
