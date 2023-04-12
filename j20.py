def get_valid_input(prompt, error_prompt, min_value=1):
    
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value < min_value:
                raise ValueError
            return value
        except ValueError:
            print(error_prompt)

def calculate_daily_count(start_count, AverageIncrease):

    daily_count = start_count
    yield daily_count
    for day in range(1, days+1):
        daily_count += daily_count * (AverageIncrease / 100)
        yield daily_count

first_count = get_valid_input("Enter the starting number of organisms/species: ", "Please enter a positive integer.")
avg_daily_percentage_increase = get_valid_input("Enter the average daily percentage increase: ", "Please enter a positive integer.")
days = get_valid_input("Enter the number of days worth of data to be printed: ", "Please enter a positive integer.")

print("Day\tOrganisms/Species Count")
for day, count in enumerate(calculate_daily_count(first_count, avg_daily_percentage_increase), start=1):
    if day > days:
        break
    print(f"{day:02d}\t{count:,.2f}")
