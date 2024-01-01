try:
    # Ask for the number of years
    num_years = int(input("Enter number of years: "))

    total_rainfall = 0  # Total inches of rainfall for all months and years
    num_months = num_years * 12  # Total number of months over the years

    # Outer loop iterates once for each year
    for year in range(num_years):
        # Inner loop iterates twelve times for each month
        for month in range(12):
            # Ask the user for the inches of rainfall for that month
            while True:
                rainfall = float(input(f"Enter amount of rainfall ({month+1}): "))
                if rainfall >= 0:
                    break
                else:
                    print("Error: Rainfall cannot be less than zero")

            # Add the rainfall for the current month to the total
            total_rainfall += rainfall

    # Calculate the average rainfall per month
    avg_rainfall = total_rainfall / num_months

    # Display the results
    print(f"Total number of months: {num_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {avg_rainfall:.2f}")
except ValueError:
    print("Please enter a correct value")