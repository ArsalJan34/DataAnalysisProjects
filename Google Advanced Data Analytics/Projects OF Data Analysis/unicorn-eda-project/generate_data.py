import pandas as pd

# Creating a subset of sample data representing the Unicorn_Companies.csv dataset
data = {
    "Company": [
        "Bytedance", "SpaceX", "SHEIN", "Stripe", "Klarna", "Canva",
        "Checkout.com", "Instacart", "JUUL Labs", "Databricks",
        "Aiven", "Jusfoun Big Data", "Innovaccer", "Algolia", "SouChe Holdings"
    ],
    "Valuation": [
        "$180B", "$100B", "$100B", "$95B", "$46B", "$40B",
        "$40B", "$39B", "$38B", "$38B",
        "$2B", "$2B", "$3B", "$2B", "$3B"
    ],
    "Date Joined": [
        "4/7/17", "12/1/12", "7/3/18", "1/23/14", "12/12/11", "1/8/18",
        "5/2/19", "12/30/14", "12/20/17", "2/5/19",
        "10/18/21", "7/9/18", "2/19/21", "7/28/21", "11/1/17"
    ],
    "Industry": [
        "Artificial intelligence", "Other", "E-commerce & direct-to-consumer", "Fintech", "Fintech", "Internet software & services",
        "Fintech", "Supply chain, logistics, & delivery", "Consumer & retail", "Data management & analytics",
        "Internet software & services", "Data management & analytics", "Health", "Internet software & services", "E-commerce & direct-to-consumer"
    ],
    "City": [
        "Beijing", "Hawthorne", "Shenzhen", "San Francisco", "Stockholm", "Surry Hills",
        "London", "San Francisco", "San Francisco", "San Francisco",
        "Helsinki", "Beijing", "San Francisco", "San Francisco", "Hangzhou"
    ],
    "Country/Region": [
        "China", "United States", "China", "United States", "Sweden", "Australia",
        "United Kingdom", "United States", "United States", "United States",
        "Finland", "China", "United States", "United States", "China"
    ],
    "Continent": [
        "Asia", "North America", "Asia", "North America", "Europe", "Oceania",
        "Europe", "North America", "North America", "North America",
        "Europe", "Asia", "North America", "North America", "Asia"
    ],
    "Year Founded": [
        2012, 2002, 2008, 2010, 2005, 2012,
        2012, 2012, 2015, 2013,
        2016, 2010, 2014, 2012, 2012
    ],
    "Funding": [
        "$8B", "$7B", "$2B", "$2B", "$4B", "$572M",
        "$2B", "$3B", "$14B", "$3B",
        "$210M", "$137M", "$379M", "$334M", "$1B"
    ],
    "Select Investors": [
        "Sequoia Capital China, SIG Asia Investments, SoftBank Group",
        "Founders Fund, Draper Fisher Jurvetson, Rothenberg Ventures",
        "Tiger Global Management, Sequoia Capital China, Shunwei Capital Partners",
        "Khosla Ventures, LowercaseCapital, capitalG",
        "Institutional Venture Partners, Sequoia Capital, General Atlantic",
        "Sequoia Capital China, Blackbird Ventures, Matrix Partners",
        "Tiger Global Management, Insight Partners, DST Global",
        "Khosla Ventures, Kleiner Perkins Caufield & Byers, VALOR EQUITY PARTNERS",
        "Tiger Global Management",
        "Andreessen Horowitz, New Enterprise Associates, Battery Ventures",
        "Institutional Venture Partners, Atomico, Earlybird Venture Capital",
        "Boxin Capital, DT Capital Partners, IDG Capital",
        "M12, WestBridge Capital, Lightspeed Venture Partners",
        "Accel, Alven Capital, Storm Ventures",
        "Morningside Ventures, Warburg Pincus, CreditEase Fintech Investment Fund"
    ]
}

# Convert dictionary to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("Unicorn_Companies.csv", index=False)
print("Unicorn_Companies.csv successfully created!")
