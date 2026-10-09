import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum,dogecoin",
    "vs_currencies": "usd,inr"
}

try:
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    for coin, prices in data.items():
        print("\n", coin.upper())
        print("USD:", prices.get("usd", "N/A"))
        print("INR:", prices.get("inr", "N/A"))

except requests.RequestException as e:
    print("Unable to fetch prices:", e)
