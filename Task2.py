# Predefined stock prices (hardcoded)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

total = 0

print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not available!")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    total += stock_prices[stock] * quantity

print("Total Investment Value:", total)

# Save result to file
with open("result.txt", "w") as file:
    file.write("Total Investment Value: " + str(total))

print("Saved to result.txt")