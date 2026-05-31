import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/smartwatch_dataset.csv")

# -------------------------------
# DATA CLEANING
# -------------------------------

# Clean Price column
df["Price (USD)"] = (
    df["Price (USD)"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price (USD)"] = pd.to_numeric(
    df["Price (USD)"],
    errors="coerce"
)

# Clean Battery Life
df["Battery Life (days)"] = pd.to_numeric(
    df["Battery Life (days)"],
    errors="coerce"
)

# Clean Water Resistance
df["Water Resistance (meters)"] = pd.to_numeric(
    df["Water Resistance (meters)"],
    errors="coerce"
)

print("=" * 50)
print("SMARTWATCH DATA ANALYSIS PROJECT")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# -------------------------------
# MOST EXPENSIVE WATCH
# -------------------------------

print("\nMost Expensive Watch:")
print(df.loc[df["Price (USD)"].idxmax()])

# -------------------------------
# CHEAPEST WATCH
# -------------------------------

print("\nCheapest Watch:")
print(df.loc[df["Price (USD)"].idxmin()])

# -------------------------------
# TOP 10 EXPENSIVE BRANDS
# -------------------------------

avg_price = df.groupby("Brand")["Price (USD)"].mean()

print("\nTop 10 Most Expensive Brands:")
print(avg_price.sort_values(ascending=False).head(10))

plt.figure(figsize=(10,5))
avg_price.sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Brands by Average Price")
plt.xlabel("Brand")
plt.ylabel("Average Price (USD)")
plt.tight_layout()
plt.savefig("charts/price_analysis.png")
plt.show()

# -------------------------------
# PRICE DISTRIBUTION
# -------------------------------

plt.figure(figsize=(10,5))
plt.hist(df["Price (USD)"].dropna(), bins=20)
plt.title("Price Distribution")
plt.xlabel("Price (USD)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/price_distribution.png")
plt.show()

# -------------------------------
# DISPLAY TYPE ANALYSIS
# -------------------------------

display_counts = df["Display Type"].value_counts()

plt.figure(figsize=(8,8))
display_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Display Type Distribution")
plt.ylabel("")
plt.savefig("charts/display_type_pie.png")
plt.show()

# -------------------------------
# BATTERY LIFE ANALYSIS
# -------------------------------

battery = (
    df.groupby("Brand")["Battery Life (days)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Brands by Battery Life:")
print(battery)

plt.figure(figsize=(10,5))
battery.plot(kind="bar")
plt.title("Top 10 Brands by Battery Life")
plt.xlabel("Brand")
plt.ylabel("Battery Life (Days)")
plt.tight_layout()
plt.savefig("charts/battery_analysis.png")
plt.show()

# -------------------------------
# BATTERY DISTRIBUTION
# -------------------------------

plt.figure(figsize=(10,5))
plt.hist(df["Battery Life (days)"].dropna(), bins=15)
plt.title("Battery Life Distribution")
plt.xlabel("Days")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/battery_distribution.png")
plt.show()

# -------------------------------
# GPS ANALYSIS
# -------------------------------

gps_count = df["GPS"].value_counts()

plt.figure(figsize=(7,7))
gps_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("GPS Availability")
plt.ylabel("")
plt.savefig("charts/gps_analysis.png")
plt.show()

# -------------------------------
# NFC ANALYSIS
# -------------------------------

nfc_count = df["NFC"].value_counts()

plt.figure(figsize=(7,7))
nfc_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("NFC Availability")
plt.ylabel("")
plt.savefig("charts/nfc_analysis.png")
plt.show()

# -------------------------------
# OPERATING SYSTEM ANALYSIS
# -------------------------------

os_count = df["Operating System"].value_counts().head(10)

plt.figure(figsize=(10,5))
os_count.plot(kind="bar")
plt.title("Top Operating Systems")
plt.xlabel("Operating System")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/os_analysis.png")
plt.show()

# -------------------------------
# TOP BRANDS
# -------------------------------

top_brands = df["Brand"].value_counts().head(10)

print("\nTop 10 Brands:")
print(top_brands)

plt.figure(figsize=(10,5))
top_brands.plot(kind="bar")
plt.title("Top 10 Smartwatch Brands")
plt.xlabel("Brand")
plt.ylabel("Number of Models")
plt.tight_layout()
plt.savefig("charts/top_brands.png")
plt.show()

# -------------------------------
# WATER RESISTANCE ANALYSIS
# -------------------------------

water = (
    df.groupby("Brand")["Water Resistance (meters)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
water.plot(kind="bar")
plt.title("Top Brands by Water Resistance")
plt.xlabel("Brand")
plt.ylabel("Meters")
plt.tight_layout()
plt.savefig("charts/water_resistance.png")
plt.show()

print("\nAll charts generated successfully!")
print("Check the charts folder.")