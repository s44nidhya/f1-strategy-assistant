import streamlit as st
import pandas as pd
import random
import joblib
from core.race_state import RaceState
import altair as alt
import time

# Load trained model
predictor = joblib.load("models/lap_time_predictor.pkl")

# Basic config
drivers = ["Hamilton", "Verstappen", "Norris", "Leclerc", "Russell"]
total_laps = 10

# Initialize session state
if "race" not in st.session_state:
    st.session_state.race = RaceState(drivers, total_laps)
    st.session_state.lap_data = []
    st.session_state.current_lap = 1
    st.session_state.auto_play = False

# Streamlit layout
st.set_page_config(page_title="F1 Race Strategy Simulator", layout="wide")
st.title("🏁 F1 Lap-by-Lap Race Simulator")

# Buttons
col1, col2, col3 = st.columns(3)

if col1.button("▶️ Next Lap"):
    st.session_state.current_lap += 1

if col2.button("🔄 Reset Race"):
    st.session_state.race = RaceState(drivers, total_laps)
    st.session_state.lap_data = []
    st.session_state.current_lap = 1
    st.session_state.auto_play = False

if col3.button("⏯ Auto Play"):
    st.session_state.auto_play = True

# Run one lap of the simulation
if st.session_state.current_lap <= total_laps:
    lap = st.session_state.current_lap
    race = st.session_state.race

    for driver in drivers:
        compound = race.drivers[driver]["compound"]
        tire_age = race.drivers[driver]["tire_age"]

        input_df = pd.DataFrame([{
            "compound": compound,
            "tire_age": tire_age
        }])

        lap_time = predictor.predict(input_df)[0]
        lap_time += random.uniform(-0.2, 0.2)

        # Pit strategy (custom logic example)
        if lap == 5 and driver == "Hamilton":
            race.update_driver(driver, lap_time + 20, compound="SOFT", pitted=True)
        else:
            race.update_driver(driver, lap_time)

        st.session_state.lap_data.append({
            "lap": lap,
            "driver": driver,
            "compound": compound,
            "lap_time": round(lap_time, 2),
            "tire_age": race.drivers[driver]["tire_age"],
            "total_time": race.drivers[driver]["total_time"]
        })

    race.next_lap()

    if st.session_state.auto_play and lap < total_laps:
        time.sleep(1)
        st.experimental_rerun()

# DataFrame of lap data
df = pd.DataFrame(st.session_state.lap_data)

# Lap time chart
st.subheader("📉 Lap Times by Driver")
if not df.empty:
    chart = alt.Chart(df).mark_line(point=True).encode(
        x="lap:O",
        y="lap_time:Q",
        color="driver:N"
    ).properties(width=800, height=400)
    st.altair_chart(chart)

# Tire degradation chart
st.subheader("📊 Tire Degradation Chart")
if not df.empty:
    tire_chart = alt.Chart(df).mark_line(point=True).encode(
        x="tire_age:Q",
        y="lap_time:Q",
        color="compound:N",
        tooltip=["driver", "compound", "tire_age", "lap_time"]
    ).properties(width=700, height=400)
    st.altair_chart(tire_chart)

# Final standings
if st.session_state.current_lap > total_laps:
    st.subheader("🏁 Final Standings")
    final = df[df["lap"] == total_laps].sort_values("total_time")
    final["gap"] = final["total_time"] - final["total_time"].min()
    st.dataframe(final[["driver", "total_time", "gap", "compound", "tire_age"]].reset_index(drop=True))
