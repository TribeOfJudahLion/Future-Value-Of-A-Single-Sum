import matplotlib.pyplot as plt

def calculate_future_value(pv, rate, years, compoundings_per_year=1):
    """
    Calculate the future value of an investment.

    :param pv: Present Value (initial investment)
    :param rate: Annual interest rate (as a decimal)
    :param years: Number of years for the investment
    :param compoundings_per_year: Number of times the interest is compounded per year
    :return: Future value of the investment
    """
    fv = pv * ((1 + rate/compoundings_per_year) ** (years * compoundings_per_year))
    return fv

def plot_investment_growth(pv, rate, years, compoundings_per_year):
    """
    Plot the growth of the investment over time.

    :param pv: Present Value (initial investment)
    :param rate: Annual interest rate (as a decimal)
    :param years: Number of years for the investment
    :param compoundings_per_year: Number of times the interest is compounded per year
    """
    times = [i/compoundings_per_year for i in range(int(years * compoundings_per_year + 1))]
    values = [calculate_future_value(pv, rate, t, compoundings_per_year) for t in times]

    plt.figure(figsize=(10, 6))
    plt.plot(times, values, '-o', color='blue')
    plt.title('Investment Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Future Value')
    plt.grid(True)
    plt.show()

# Example usage
present_value = 10000  # $10,000 initial investment
annual_interest_rate = 0.05  # 5% annual interest rate
investment_period_years = 10  # Investment period of 10 years
compoundings_per_year = 4  # Quarterly compounding

# Calculate future value
future_value = calculate_future_value(present_value, annual_interest_rate, investment_period_years, compoundings_per_year)
print(f"Future Value: ${future_value:.2f}")

# Plot the investment growth
plot_investment_growth(present_value, annual_interest_rate, investment_period_years, compoundings_per_year)
