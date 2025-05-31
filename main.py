import random
from core.race_state import RaceState

# Step 1: Create race with 5 drivers, 10 laps
drivers = ["Hamilton", "Verstappen", "Norris", "Leclerc", "Russell"]
total_laps = 10

race = RaceState(drivers, total_laps)

# Step 2: Simulate 10 laps
for lap in range(total_laps):
    print(f"\n🟢 Lap {lap + 1} Start")

    for driver in drivers:
        # Random base lap time + compound wear effect
        base = random.uniform(85, 88)  # seconds
        tire_wear_penalty = race.drivers[driver]["tire_age"] * 0.1
        lap_time = round(base + tire_wear_penalty, 2)

        # Random pit stop on Lap 5
        if lap == 4 and driver == "Hamilton":
            print(f"🔧 {driver} pits for SOFT tires!")
            race.update_driver(driver, lap_time + 20, compound="SOFT", pitted=True)
        else:
            race.update_driver(driver, lap_time)

    race.next_lap()

    # Print positions
    sorted_drivers = sorted(race.drivers.items(), key=lambda x: x[1]["position"])
    for name, data in sorted_drivers:
        print(f"{data['position']:>2}. {name:10} | Total: {data['total_time']:.2f}s | Tires: {data['compound']} | Age: {data['tire_age']}")


#model 
import joblib

# Load model
predictor = joblib.load("models/lap_time_predictor.pkl")

# Replace lap time generation in your loop:
for driver in drivers:
    compound = race.drivers[driver]["compound"]
    tire_age = race.drivers[driver]["tire_age"]

    # Predict lap time using ML model
    lap_time = predictor.predict([[compound, tire_age]])[0]

    # Optional: add tiny randomness for realism
    lap_time += random.uniform(-0.2, 0.2)

    # Pit logic
    if lap == 4 and driver == "Hamilton":
        race.update_driver(driver, lap_time + 20, compound="SOFT", pitted=True)
    else:
        race.update_driver(driver, lap_time)
