import requests
import pandas as pd
import os

# -----------------------------
# Replace with your own API key
# -----------------------------
API_KEY = "a94c8e39d59949818b4962ebe1bacc68"

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# API endpoint
url = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

# Query parameters
params = {
    "reporterCode": "364",
    "period": "2022",
    "cmdCode": "TOTAL",
    "flowCode": "M",
    "partnerCode": "0",
    "partner2Code": "0",
    "maxRecords": 500
}

# Correct headers (dictionary, NOT a set)
headers = {
    "Ocp-Apim-Subscription-Key": API_KEY
}

try:
    response = requests.get(url, params=params, headers=headers)

    print("Status Code:", response.status_code)

    # Show the raw response if something went wrong
    if response.status_code != 200:
        print(response.text)
        exit()

    data = response.json()

    if "data" not in data:
        print("No 'data' field found in the response.")
        print(data)
        exit()

    df = pd.DataFrame(data["data"])

    print(df.head())

    output_file = "data/raw/comtrade_2023.csv"
    df.to_csv(output_file, index=False)

    print(f"\nDownloaded {len(df)} records.")
    print(f"Saved to: {output_file}")

except requests.exceptions.RequestException as e:
    print("Request failed:")
    print(e)




url = "https://comtradeapi.un.org/public/v1/get/C/A/HS"

params = {
    "reporterCode": "364"
}

r = requests.get(url, params=params)

print(r.text[:1000])