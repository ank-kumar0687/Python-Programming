import matplotlib.pyplot as plt


profits = []
years = []

for i in range(1, 6):
    year = input(f"Enter Year {i}: ")
    profit = float(input(f"Enter Profit for {year}: "))
    
    years.append(year)
    profits.append(profit)

# Plot line graph
plt.plot(years, profits, marker='o')

# Labels and title
plt.xlabel("Years")
plt.ylabel("Profit")
plt.title("Profit of 5 Years")

# Show grid
plt.grid()

# Display graph
plt.show()
