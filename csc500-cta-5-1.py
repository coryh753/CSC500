try:
    # Ask for the number of years
    numYears = int(input("Enter number of years: "))

    totalRainfall = 0  # Total inches of rainfall for all months and years
    numMonths = numYears * 12  # Total number of months over the years

    # Outer loop iterates once for each year
    for year in range(numYears):
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
            totalRainfall += rainfall

    # Calculate the average rainfall per month
    avgRainfall = totalRainfall / numMonths

    # Display the results
    print(f"Total number of months: {numMonths}")
    print(f"Total inches of rainfall: {totalRainfall}")
    print(f"Average rainfall per month: {avgRainfall:.2f}")
except ValueError:
    print("Please enter a correct value")