class RaceState:
    def __init__(self, drivers, total_laps):
        self.lap = 1
        self.total_laps = total_laps
        self.weather = "dry"
        self.safety_car = False

        self.drivers = {
            name: {
                "position": i + 1,
                "lap_time": 0,
                "total_time": 0,
                "tire_age": 0,
                "compound": "MEDIUM",
                "laps": [],
            }
            for i, name in enumerate(drivers)
        }

    def update_driver(self, name, lap_time, compound=None, pitted=False):
        d = self.drivers[name]
        d["lap_time"] = lap_time
        d["total_time"] += lap_time
        d["laps"].append(lap_time)
        d["tire_age"] += 1

        if pitted:
            d["tire_age"] = 0
            d["compound"] = compound

    def next_lap(self):
        self.lap += 1
        self._recalculate_positions()

    def _recalculate_positions(self):
        sorted_drivers = sorted(self.drivers.items(), key=lambda x: x[1]["total_time"])
        for i, (name, _) in enumerate(sorted_drivers):
            self.drivers[name]["position"] = i + 1
