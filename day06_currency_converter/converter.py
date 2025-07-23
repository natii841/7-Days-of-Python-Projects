# Day 6 - Currency Converter (Offline Example)

# For live rates, you'd use an API like exchangerate-api.com or fixer.io
# Here we'll use fixed conversion rate for simplicity

rate_usd_to_eur = 0.85
usd = float(input("Enter USD amount: "))
eur = usd * rate_usd_to_eur
print(f"{usd} USD is {eur:.2f} EUR")
