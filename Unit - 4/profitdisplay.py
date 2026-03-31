import matplotlib.pyplot as plt


years = []
profits = []

print("Enter profit for 5 years:")

for i in range(1, 6):
    year = input(f"Enter Year {i}: ")
    profit = float(input(f"Enter Profit for {year}: "))
    
    years.append(year)
    profits.append(profit)


plt.plot(years, profits, marker='o')


plt.xlabel("Year")
plt.ylabel("Profit")
plt.title("Profit of 5 Years")


plt.grid()


plt.show()
