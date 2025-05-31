# Create a dictionary with country-capital pairs
countries = {
	"India": "New Delhi",
	"USA": "Washington D.C.",
	"France": "Paris",
	"Japan": "Tokyo"
}

print("Keys (Countries):")
for country in countries.keys():
	print(country)

print("\nValues (Capitals):")
for capital in countries.values():
	print(capital)

print("\nCountry - Capital:")
for country, capital in countries.items():
	print(f"{country} → {capital}")
