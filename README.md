
#  F1 Strategy Assistant

An intelligent, data-driven strategy simulator for Formula 1 races that integrates machine learning, probabilistic modeling, and real-time telemetry to assist with pit stop decision-making and tire degradation forecasting.

##  Overview

This project provides a real-time strategy assistant designed for use during Formula 1 races. It leverages Bayesian regression and reinforcement learning to simulate race scenarios, evaluate tire degradation, and recommend optimal pit stop strategies based on actual telemetry data.

##  Key Features

-  **Tire Degradation Modeling:** Compound-specific degradation curves built using Bayesian regression with uncertainty quantification.
-  **Reinforcement Learning Agent:** Trained to determine optimal pit strategies by simulating various race conditions and tire performance.
-  **Telemetry Integration:** Utilizes the FastF1 API to ingest and process real race data for accurate modeling and simulations.
-  **Multi-Strategy Simulation:** Simulates and compares multiple pit stop strategies dynamically during race conditions.
-  **Interactive Dashboard:** Built using Streamlit to visualize race strategy, tire wear, and performance projections in real time.

##  Project Structure

f1-strategy-assistant/
├── data/ # Raw and preprocessed FastF1 data
├── notebooks/ # Development and exploratory notebooks
├── src/
│ ├── degradation_model/ # Bayesian and polynomial tire modeling
│ ├── strategy_sim/ # Reinforcement learning and simulation logic
│ ├── visualizations/ # Plotting and graphing utilities
│ └── app/ # Streamlit-based interface
├── requirements.txt
├── main.py
└── README.md

## Technologies Used
Python | Scikit-learn | Streamlit | FastF1

Bayesian Regression for modeling tire wear

Q-Learning / Custom RL Agent for pit strategy optimization

Matplotlib / Seaborn for visual analysis

## Potential Enhancements
Incorporate live timing and weather data for real-time adaptive strategy

Expand multi-agent strategy simulations

Model compound switching penalties and undercut/overcut effectiveness

##  Getting Started

```bash
git clone https://github.com/s44nidhya/f1-strategy-assistant.git
cd f1-strategy-assistant
pip install -r requirements.txt
streamlit run src/app/main.py

