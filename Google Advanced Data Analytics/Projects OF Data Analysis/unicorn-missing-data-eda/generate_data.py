import pandas as pd
import numpy as np

# generates pseudo random numbers using starting seed fixing the seed to 42 guarantees that every time you run this script it produces random numbers
np.random.seed(42)

companies_list = ["Bytedance", "SpaceX", "SHEIN", "Stripe", "Klarna", "Canva", "Checkout.com", "Instacart"]
industries = ["Hardware", "Artificial intelligence", "Fintech", "E-commerce & direct-to-consumer", "Internet software & services", "Mobile & telecommunications", "Supply chain, logistics, & delivery"]
cities = ["Beijing", "San Francisco", "London", "Shenzhen", "Stockholm", "New York", "Paris"]
countries = ["United States", "China", "India", "United Kingdom", "Germany", "Sweden", "Australia", "France", "Canada", "Bahamas", "Singapore", "Hong Kong"]
# total rows to generate
num_records = 1074

data = {
    "Company": [f"Company_{i}" for i in range(num_records)],
    "Valuation": [f"${np.random.randint(1, 180)}B" for _ in range(num_records)],
    "Date Joined": pd.date_range(start="2011-01-01", end="2022-03-31", periods=num_records).strftime('%m/%d/%y'),
    "Industry": np.random.choice(industries, size=num_records),
    "City": np.random.choice(cities, size=num_records),
    "Country/Region": np.random.choice(countries, size=num_records),
    "Continent": ["North America" if c in ["United States", "Canada", "Bahamas"] else "Asia" if c in ["China", "India", "Singapore", "Hong Kong"] else "Europe" for c in np.random.choice(countries, size=num_records)],
    "Year Founded": np.random.randint(1919, 2022, size=num_records),
    "Funding": [f"${np.random.randint(100, 900)}M" for _ in range(num_records)],
    "Select Investors": ["Sequoia Capital, SoftBank, Accel" for _ in range(num_records)]
}
df = pd.DataFrame(data)
df.loc[np.random.choice(df.index, 16, replace=False), 'City'] = np.nan
df.loc[np.random.choice(df.index, 1, replace=False), 'Select Investors'] = np.nan
df.loc[36, ['Company', 'Valuation', ...]] = ['Bitmain', '$12B', ...]
df.loc[1243, ['Company', 'Valuation', ...]] = ['Global Switch', '$11B', ...]
df.loc[1873, ['Company', 'Valuation', ...]] = ['BenevolentAI', '$1B', ...]
df.to_csv("Unicorn_Companies.csv", index=False)
print("Unicorn_Companies.csv successfully created!")
