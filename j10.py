# Defining list
rainfall = []

numberofyears = int(input("Enter the number of years = "))

for year in range(1, numberofyears + 1):
    print(f"\nYear {year}:")
    Monthly_Rainfall = []
    for month in range(1, 13):
        rainfall_cm = float(input(f"Enter the rainfall in (cm) for month {month}: "))
        Monthly_Rainfall.append(rainfall_cm)
    rainfall.append(Monthly_Rainfall)

for year, rainfall_data in enumerate(rainfall, start=1):
    total_rainfall = sum(rainfall_data)
    avg_monthly_rainfall = total_rainfall / 12
    print(f"\nYear {year} Rainfall Data:")
    print(f"Total rainfall: {total_rainfall:.2f} cm")
    print(f"Average monthly rainfall: {avg_monthly_rainfall:.2f} cm")
