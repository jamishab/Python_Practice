import matplotlib.pyplot as plt # Import matplotlib

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 220, 350, 580, 800, 1100, 1300, 1250, 900, 500, 300, 250]
temp = [5, 7, 12, 18, 22, 28, 32, 31, 24, 15, 9, 6]

# Adding strings
xlab = 'Months [2025]'
ylab = 'Sales'
title = '2025 Monthly Sales'
# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# Add title
plt.title(title)


# Create line plot
plt.plot(months, sales, c = 'purple')
# Show plot
plt.show()
# Clean plot
# plt.clf()
# Existing code...

# Added: histograms and scatterplots
plt.hist(sales, bins=5, color = 'pink')
plt.xlabel('Sales Ranges')
plt.ylabel('Frequency')
plt.title('Sales Distribution in 2025')
plt.show()

plt.scatter(temp, sales, color='red', alpha = 0.7)
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales')
plt.title('Sales vs Temperature in 2025')
# Add grid lines
plt.grid(True) 
plt.show()
