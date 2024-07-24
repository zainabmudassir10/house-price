import matplotlib.pyplot as plt


prices = [300000, 350000, 400000, 250000, 500000]
sizes = [1500, 1600, 1800, 1400, 2000]

# Scatter Plot of Price vs. Size
plt.scatter(sizes, prices, color='blue')
plt.title('Price vs Size')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price')
plt.show()
