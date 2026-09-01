# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 170
}

total_investment = 0
print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))
while True:
    stock = input("Enter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        total_investment += stock_prices[stock] * quantity

        print(f"{stock}: {quantity} × ${stock_prices[stock]} = ${total_investment}")
    else:
        print("Stock not available!")

print("\nTotal Investment Value: $", total_investment)

# Save result to file
with open("portfolio_summary.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved in portfolio_summary.txt")
