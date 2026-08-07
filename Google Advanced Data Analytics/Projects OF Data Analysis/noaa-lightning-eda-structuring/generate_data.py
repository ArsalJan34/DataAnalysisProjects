import pandas as pd
import numpy as np

# setting seed for reproductcibilty
# this initializes numpy random number generator with constant starting point 42 this ensures every run generates the exact same sequence of random values
np.random.seed(42)

# defines a custom function which is prolly reusable it takes 4 parameters
def generate_lightning_data(start_date, end_date, num_rows, filename):
  # pd.range_range generates a continuos sequence of daily dates from start to end Frequency D meany dailt freq
  dates = pd.date_range(start=start_date, end=end_date, freq='D')
  # this randomly selects dates from teh dates array with replacment until it accumulates an array of length num_rows
  random_dates = np.random.choice(dates, size=num_rows)

  # np.random.exponential(scale=20,size=num_rows) it draws random samples from an expoential distribution with a mean scale of 20 this models skewed real word data event dat where many small events occur and few large one occur
  # astype(int) converts resulting floating point decimal numbers inot whole intergers by dropping decimal parts.
  # +1 adds 1 to every integer to guarantee that every row has at least 1 strike avoiding 0- strike records
  # Generate realistic strike counts and geographic center points
  strikes = np.random.exponential(scale=20, size=num_rows).astype(int) + 1
  # np.random.uniform(-120,-70,size=num_rows): Generates random decimal longitudes uniformly distributed between -120.0 and -70.0 (covering North America)
  # np.random.uniform(20,50, size=num_rows):Generates random decimal latitudes uniformly distributed 20.0 and 50.0
  # .round(1): Rounds all generated coordinates to 1 decimal place.
  longitudes = np.random.uniform(-120, -70, size=num_rows).round(1)
  latitudes = np.random.uniform(20, 50, size=num_rows).round(1)
  # zip(longitudes, latitudes): pairs up each longitude and latitude element by element: [(-115.2,32.1), (-88.4, 41.5), ...]
  #f"POINT({lon} {lat})" formates each coordinate pair into a standard WKT (Well-known text)GIS geometry string
  center_points = [f"POINT({lon} {lat})" for lon, lat in zip(longitudes, latitudes)]
  #pd.DataFrame({...}): Constructs a Pandas DataFrame from a dictionary:
  # 'date': Converts random_dates into datetime format via pd.to_datetime() and formats them into standard 'YYYY-MM-DD' date strings using .strftime('%Y-%m-%d').
  # 'number_of_strikes': Populates the column with the strikes array.
  # 'center_point_geom': Populates the column with the center_points list.
  df = pd.DataFrame({
        'date': pd.to_datetime(random_dates).strftime('%Y-%m-%d'),
        'number_of_strikes': strikes,
        'center_point_geom': center_points
    })
  # df.to_csv(filename, index=False): Writes the DataFrame to a file named filename. index=False prevents writing Pandas row index numbers as an extra column.
  # print(...): Prints a message confirming successful creation of the file and reporting row counts.
  df.to_csv(filename, index=False)
  print(f"File '{filename}' successfully created with {num_rows} rows.")
  # Generate 2018 dataset (dataset1)
generate_lightning_data("2018-01-01", "2018-12-31", 10000, 'eda_structuring_with_python_dataset1.csv')

# Generate 2016-2017 dataset (dataset2)
generate_lightning_data("2016-01-01", "2017-12-31", 15000, 'eda_structuring_with_python_dataset2.csv')
