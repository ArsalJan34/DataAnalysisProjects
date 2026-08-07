import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate date range covering 2016 through 2018
dates = pd.date_range(start="2016-01-01", end="2018-12-31", freq="D")

# Repeat dates to simulate multiple spatial recordings per day
dates_expanded = np.repeat(dates, 10)

# Generate synthetic number of strikes and spatial center points
strikes = np.random.randint(10, 5000, size=len(dates_expanded))
longitudes = np.random.uniform(-125, -65, size=len(dates_expanded)).round(1)
latitudes = np.random.uniform(25, 49, size=len(dates_expanded)).round(1)

center_points = [f"POINT({lon} {lat})" for lon, lat in zip(longitudes, latitudes)]

# Create DataFrame
df = pd.DataFrame({
    'date': dates_expanded.strftime('%Y-%m-%d'),
    'number_of_strikes': strikes,
    'center_point_geom': center_points
})

# Save to CSV
df.to_csv('eda_manipulate_date_strings_with_python.csv', index=False)
print("eda_manipulate_date_strings_with_python.csv successfully created!")
