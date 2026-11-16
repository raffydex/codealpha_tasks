"""STOCK PORTFOLIO TRACKER for CodeAlpha Internship"""

import csv

# Dictionary containing predefined stock prices.
# These are sample prices, NOT live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "NVDA": 135.00,
    "AMZN": 190.00
}

# DISPLAY WELCOME MESSAGE
def display_welcome():
    """Display the application welcome message"""

    print("=" * 50)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    print("Calculate and manage your stock investments")
    print("Note: All prices are predefined sample prices")
    print()

# DISPLAY AVAILABLE STOCKS
def display_available_stocks():
    """Display all available stocks and their prices"""

    print("\nAVAILABLE STOCKS")
    print("-" * 35)

    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:,.2f}")

    print("-" * 35)

# GET AND VALIDATE STOCK SYMBOL
def get_stock_symbol():
    """Get a valid stock symbol from the user"""

    while True:

        symbol = input(
            "\nEnter stock symbol: "
        ).strip().upper()

        # Check whether the symbol exists
        if symbol in STOCK_PRICES:
            return symbol

        print(
            "Invalid stock symbol. "
            "Please choose from the available stocks"
        )

# GET AND VALIDATE STOCK QUANTITY
def get_quantity(symbol):
    """Get a valid positive whole-number quantity"""

    while True:

        try:
            quantity = int(
                input(f"\nEnter quantity of {symbol} shares: ")
            )

            # Quantity must be greater than zero
            if quantity <= 0:
                print(
                    "Invalid quantity. "
                    "Please enter a number greater than zero"
                )
                continue

            return quantity

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid whole number"
            )

# CALCULATE STOCK INVESTMENT VALUE
def calculate_investment(symbol, quantity):
    """Calculate the total value of a stock investment"""

    stock_price = STOCK_PRICES[symbol]

    investment_value = stock_price * quantity

    return investment_value

# ADD STOCK TO PORTFOLIO
def add_stock(portfolio, symbol, quantity):
    """Add a stock or update an existing stock entry"""

    stock_price = STOCK_PRICES[symbol]

    # Check whether the stock already exists
    for stock in portfolio:

        if stock["symbol"] == symbol:

            # Combine the new quantity with the existing quantity
            stock["quantity"] += quantity

            # Recalculate the total stock value
            stock["value"] = calculate_investment(
                symbol, stock["quantity"]
            )

            print(
                f"\n{symbol} already exists in your portfolio"
            )
            print("Existing quantity has been updated")

            return stock["value"]

    # Add a new stock if it does not already exist
    investment_value = calculate_investment(
        symbol, quantity
    )

    portfolio.append({
        "symbol": symbol,
        "quantity": quantity,
        "price": stock_price,
        "value": investment_value
    })

    print(f"\n{symbol} added successfully!")

    return investment_value

# ASK USER WHETHER TO CONTINUE
def continue_selection():
    """Ask whether the user wants to add another stock"""

    while True:

        choice = input(
            "\nWould you like to add another stock? (Y/N): "
        ).strip().upper()

        if choice == "Y":
            return True

        elif choice == "N":
            return False

        else:
            print("Invalid choice. Please enter Y or N")

# CALCULATE TOTAL PORTFOLIO VALUE
def calculate_total_investment(portfolio):
    """Calculate the combined value of all portfolio stocks"""

    total = 0.0

    for stock in portfolio:
        total += stock["value"]

    return total

# DISPLAY FINAL PORTFOLIO
def display_portfolio(portfolio):
    """Display all portfolio stocks and their investment values"""

    if not portfolio:
        print("\nYour portfolio is empty")
        print("No stocks were added")
        return

    total_investment = calculate_total_investment(
        portfolio
    )

    print("\n" + "=" * 60)
    print("                 YOUR STOCK PORTFOLIO")
    print("=" * 60)

    print(
        f"{'STOCK':<12}"
        f"{'QUANTITY':<12}"
        f"{'PRICE':<16}"
        f"{'TOTAL VALUE':<16}"
    )

    print("-" * 60)

    for stock in portfolio:

        print(
            f"{stock['symbol']:<12}"
            f"{stock['quantity']:<12}"
            f"${stock['price']:<15,.2f}"
            f"${stock['value']:<15,.2f}"
        )

    print("-" * 60)

    print(
        f"TOTAL INVESTMENT: ${total_investment:,.2f}"
    )

    print("=" * 60)
    print("Thank you for using Stock Portfolio Tracker!")


# SAVE PORTFOLIO TO TXT FILE

def save_to_txt(portfolio):
    """Save portfolio results to a TXT file"""

    try:

        total_investment = calculate_total_investment(
            portfolio
        )

        with open("stock_portfolio.txt", "w") as file:

            file.write("STOCK PORTFOLIO TRACKER\n")
            file.write("=" * 50 + "\n\n")

            file.write(
                f"{'STOCK':<12}"
                f"{'QUANTITY':<12}"
                f"{'PRICE':<16}"
                f"{'TOTAL VALUE':<16}\n"
            )

            file.write("-" * 56 + "\n")

            for stock in portfolio:

                file.write(
                    f"{stock['symbol']:<12}"
                    f"{stock['quantity']:<12}"
                    f"${stock['price']:<15,.2f}"
                    f"${stock['value']:<15,.2f}\n"
                )

            file.write("-" * 56 + "\n")

            file.write(
                f"\nTOTAL INVESTMENT: ${total_investment:,.2f}\n"
            )

        print("\nPortfolio successfully saved to stock_portfolio.txt!")

    except OSError:
        print("\nError: Unable to save portfolio to TXT file")

# SAVE PORTFOLIO TO CSV FILE
def save_to_csv(portfolio):
    """Save portfolio results to a CSV file"""

    try:

        with open("stock_portfolio.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Write column headings
            writer.writerow([
                "Stock",
                "Quantity",
                "Price",
                "Total Value"
            ])

            # Write portfolio stock details
            for stock in portfolio:

                writer.writerow([
                    stock["symbol"],
                    stock["quantity"],
                    stock["price"],
                    stock["value"]
                ])

            # Write total investment
            writer.writerow([])
            writer.writerow([
                "TOTAL INVESTMENT",
                "",
                "",
                calculate_total_investment(portfolio)
            ])

        print("\nPortfolio successfully saved to stock_portfolio.csv!")

    except OSError:
        print("\nError: Unable to save portfolio to CSV file")

# ASK USER WHETHER TO SAVE PORTFOLIO
def save_portfolio(portfolio):
    """Ask the user how they want to save their portfolio"""

    while True:

        print("\nSAVE YOUR PORTFOLIO")
        print("-" * 35)
        print("1. Save as TXT")
        print("2. Save as CSV")
        print("3. Save as both TXT and CSV")
        print("4. Skip saving")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            save_to_txt(portfolio)
            break

        elif choice == "2":
            save_to_csv(portfolio)
            break

        elif choice == "3":
            save_to_txt(portfolio)
            save_to_csv(portfolio)
            break

        elif choice == "4":
            print("\nPortfolio saving skipped")
            break

        else:
            print("Invalid choice. Please select between 1 and 4")

# MAIN APPLICATION
def main():
    """Run the Stock Portfolio Tracker application"""

    display_welcome()

    display_available_stocks()

    # Create an empty list to store portfolio entries
    portfolio = []

    # Continue accepting stocks until the user finishes
    while True:

        # Get a valid stock symbol
        symbol = get_stock_symbol()

        # Get a valid quantity
        quantity = get_quantity(symbol)

        # Add the stock to the portfolio
        investment_value = add_stock(
            portfolio, symbol, quantity
        )

        print(
            f"Total investment in {symbol}: "
            f"${investment_value:,.2f}"
        )

        # Ask whether the user wants to continue
        if not continue_selection():
            break

    # Display the completed portfolio
    display_portfolio(portfolio)

    # Ask the user whether to save the portfolio
    if portfolio:
        save_portfolio(portfolio)


# PROGRAM EXECUTION
if __name__ == "__main__":
    main()
