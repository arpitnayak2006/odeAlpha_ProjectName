import csv

# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2000, "MSFT": 320, "AMZN": 130}

# Dictionary to store user portfolio
portfolio = {}

# User input for stock names and quantities
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in list! Try again.")
        continue
    quantity = input(f"Enter quantity of {stock}: ")
    if not quantity.isdigit():
        print("Invalid quantity! Enter a number.")
        continue
    portfolio[stock] = int(quantity)

# Calculate total investment value
total_investment = sum(portfolio[stock] * stock_prices[stock] for stock in portfolio)
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares at ${stock_prices[stock]} each")
print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save portfolio to CSV file
save_option = input("\nDo you want to save this to a CSV file? (yes/no): ").lower()
if save_option == "yes":
    with open("stock_portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
    print("Portfolio saved as 'stock_portfolio.csv'!")