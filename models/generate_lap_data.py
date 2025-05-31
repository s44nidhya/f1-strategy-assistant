import pandas as pd
import numpy as np

np.random.seed(42)

drivers = ["Hamilton", "Verstappen", "Leclerc", "Russell", "Norris"]
compounds = ["SOFT", "MEDIUM", "HARD"]
compound_base = {"SOFT": 85, "MEDIUM": 87, "HARD": 89}

data = []

for driver in drivers:
    for compound in compounds:
        for age in range(1, 31):  # Up to 30 laps
            base_time = compound_base[compound]
            degradation = 0.15 * age  # Tire gets slower with age
            skill_offset = np.random.normal(0, 0.3)
            noise = np.random.normal(0, 0.4)

            lap_time = base_time + degradation + skill_offset + noise

            data.append({
                "driver": driver,
                "compound": compound,
                "tire_age": age,
                "lap_time": lap_time
            })

df = pd.DataFrame(data)
df.to_csv("data/lap_data.csv", index=False)
print("✅ Lap data generated.")
