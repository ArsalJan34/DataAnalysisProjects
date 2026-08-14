import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate sample unicorn dataset
companies_list = [
    "Bytedance", "SpaceX", "SHEIN", "Stripe", "Klarna", "Canva",
    "Checkout.com", "Instacart", "JUUL Labs", "Databricks",
    "Phantom", "Yidian Zixun", "GlobalBees", "ClickHouse", "LayerZero Labs",
    "Flink Food", "Aptos", "Yuga Labs", "Jokr", "Mensa Brands",
    "FTX", "J&T Express", "Blockchain.com", "OpenSea", "Getir"
]

industries = [
    "Artificial intelligence", "Other", "E-commerce & direct-to-consumer",
    "Fintech", "Internet software & services", "Supply chain, logistics, & delivery",
    "Consumer & retail", "Data management & analytics", "Mobile & telecommunications"
]

cities = ["San Francisco", "Beijing", "New York", "London", "Shenzhen", "Berlin", "Bengaluru"]
countries = ["United States", "China", "United Kingdom", "Germany", "India"]
continents = ["North America", "Asia", "Europe"]

num_records = 300
data = {
    "Company": [f"Company_{i}" for i in range(num_records)],
    "Valuation": [f"${np.random.randint(1, 50)}B" for _ in range(num_records)],
    "Date Joined": pd.date_range(start="2010-01-01", end="2026-03-31", periods=num_records).strftime('%m/%d/%y'),
    "Industry": np.random.choice(industries, size=num_records),
    "City": np.random.choice(cities, size=num_records),
    "Country/Region": np.random.choice(countries, size=num_records),
    "Continent": np.random.choice(continents, size=num_records),
    "Year Founded": np.random.randint(1995, 2022, size=num_records),
    "Funding": [f"${np.random.randint(100, 900)}M" for _ in range(num_records)],
    "Select Investors": ["Sequoia Capital, Tiger Global, Accel" for _ in range(num_records)]
}

# Overwrite top rows to match explicit lab examples
df = pd.DataFrame(data)
df.loc[0:4, "Company"] = ["Bytedance", "SpaceX", "SHEIN", "Stripe", "Klarna"]
df.loc[0:4, "Valuation"] = ["$180B", "$100B", "$100B", "$95B", "$46B"]
df.loc[0:4, "Date Joined"] = ["4/7/17", "12/1/12", "7/3/18", "1/23/14", "12/12/11"]

df.to_csv("Unicorn_Companies.csv", index=False)
print("Unicorn_Companies.csv successfully created!")
