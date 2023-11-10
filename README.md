<br/>
<p align="center">
  <a href="https://github.com//Future-Value-Of-A-Single-Sum">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Unlock the Future of Finance: Master TVM with Our Future Value Calculator</h3>

  <p align="center">
    Empower Your Financial Decisions – Explore the Potential of Every Dollar!
    <br/>
    <br/>
    <a href="https://github.com//Future-Value-Of-A-Single-Sum"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com//Future-Value-Of-A-Single-Sum">View Demo</a>
    .
    <a href="https://github.com//Future-Value-Of-A-Single-Sum/issues">Report Bug</a>
    .
    <a href="https://github.com//Future-Value-Of-A-Single-Sum/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads//Future-Value-Of-A-Single-Sum/total) ![Contributors](https://img.shields.io/github/contributors//Future-Value-Of-A-Single-Sum?color=dark-green) ![Stargazers](https://img.shields.io/github/stars//Future-Value-Of-A-Single-Sum?style=social) ![Issues](https://img.shields.io/github/issues//Future-Value-Of-A-Single-Sum) ![License](https://img.shields.io/github/license//Future-Value-Of-A-Single-Sum) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Statement:

Suppose an individual named Alex wants to invest a sum of money with the goal of funding their child's education in 10 years. Alex has $10,000 available to invest and is considering a fixed deposit account that compounds interest quarterly. The account offers an annual interest rate of 5%. Alex wishes to know the future value of the investment after 10 years and wants to visualize how the investment will grow over time to ensure that it will meet the anticipated education costs.

Alex requires a solution that will allow them to:
1. Calculate the future value of the investment after 10 years.
2. Plot the growth of the investment at each compounding period to visualize the compounding effect over time.

### Solution:

To address Alex's needs, we can use the provided Python code, which contains two functions that work together to solve the problem:

1. `calculate_future_value(pv, rate, years, compoundings_per_year)`:
   - This function calculates the future value of the investment by taking into account the present value, annual interest rate, investment duration, and the frequency of compounding.
   - The formula used is a standard compound interest formula: 
     \[ FV = PV \times \left(1 + \frac{rate}{compoundings\_per\_year}\right)^{years \times compoundings\_per\_year} \]

2. `plot_investment_growth(pv, rate, years, compoundings_per_year)`:
   - This function generates a time series from the start of the investment until the end, at each compounding interval, and calculates the investment value at each point using the `calculate_future_value` function.
   - It then plots these values using Matplotlib to create a visual representation of the investment growth over time.

Using the example values in the code:
- Present Value (`pv`): $10,000 (the initial investment).
- Annual Interest Rate (`rate`): 0.05 (5% interest rate).
- Investment Period Years (`years`): 10 (the period after which Alex needs the money for the education costs).
- Compoundings Per Year (`compoundings_per_year`): 4 (interest is compounded quarterly).

The `calculate_future_value` function will compute the future value to be $16,436.19. This is the amount Alex will have after 10 years. Additionally, using the `plot_investment_growth` function, Alex can see a graph that shows the exponential growth of the investment, demonstrating the effect of compounding each quarter.

By providing the future value and a visual representation of the investment growth, Alex can make an informed decision about whether this investment will meet the anticipated education costs or if they need to consider alternative investment options with potentially higher returns.

The provided code is a Python script designed to calculate and plot the growth of an investment over time using the concept of compound interest. The code consists of two main functions: `calculate_future_value` and `plot_investment_growth`. Let's break down each part of the code for a detailed understanding:

### Function: `calculate_future_value`
This function calculates the future value of an investment based on four parameters:

1. **pv (Present Value)**: The initial amount of money invested.
2. **rate (Annual Interest Rate)**: The yearly interest rate expressed as a decimal. For example, a 5% interest rate is expressed as 0.05.
3. **years (Number of Years)**: The total duration for which the investment is held.
4. **compoundings_per_year (Compounding Frequency)**: The number of times the interest is compounded per year. If not specified, it defaults to 1, indicating simple annual compounding.

The formula used in this function is:
\[ FV = PV \times \left(1 + \frac{rate}{compoundings\_per\_year}\right)^{years \times compoundings\_per\_year} \]
where \( FV \) is the future value of the investment.

### Function: `plot_investment_growth`
This function visualizes the growth of the investment over time using a line graph. It uses the same four parameters as `calculate_future_value`:

1. **pv (Present Value)**
2. **rate (Annual Interest Rate)**
3. **years (Number of Years)**
4. **compoundings_per_year (Compounding Frequency)**

The function calculates the value of the investment at various points in time and plots these values. It does this by:

- Generating a list of time points (`times`), calculated by dividing the total number of compoundings over the investment period into equal intervals.
- Calculating the future value of the investment at each of these time points using the `calculate_future_value` function.
- Plotting these values against time using Matplotlib, resulting in a graph that shows how the investment grows over time.

### Example Usage
The script includes an example that demonstrates how to use these functions:

- **Present Value (`present_value`)**: $10,000
- **Annual Interest Rate (`annual_interest_rate`)**: 5% or 0.05 in decimal
- **Investment Period Years (`investment_period_years`)**: 10 years
- **Compounding Per Year (`compoundings_per_year`)**: Quarterly (4 times a year)

The script first calculates the future value of this investment after 10 years using the `calculate_future_value` function, and then plots the growth of this investment over the 10-year period using `plot_investment_growth`.

### Key Takeaways
- The script applies the concept of compound interest to calculate the future value of an investment.
- It visualizes how the investment grows over time, which is useful for understanding the impact of compounding on investments.
- The use of Matplotlib for plotting makes the growth easily interpretable through a visual graph.

The graph titled "Investment Growth Over Time", is plotted on a 10x6 grid. The horizontal axis (X-axis) is labeled "Years" and spans from 0 to 10, indicating the time frame of the investment. The vertical axis (Y-axis) is labeled "Future Value" and displays the monetary value of the investment over time.

The blue line in the graph represents the growth of the investment, with blue dots marking the value of the investment at the end of each compounding period. The line starts at the lower left corner, indicating the initial investment value (Present Value), and curves upwards to the right, showing an increase in value over time, which is characteristic of compound interest.

The graph demonstrates that as time passes, the value of the investment increases. This increase is not linear but exponential, due to the effects of compounding—the interest earned in each period adds to the principal, resulting in interest being earned on interest in subsequent periods.

The final point on the graph is at the 10-year mark, which is the end of the investment period. The future value at this point is indicated in the output below the graph as $16,436.19. This value is the result of the initial $10,000 investment growing at an annual interest rate of 5%, compounded quarterly over 10 years.

## Built With

This repository is dedicated to a financial calculation and visualization tool that determines the future value of an investment considering compound interest. The project is built using Python and its powerful libraries for both the calculation logic and the graphical representation of data.

### Core Language

- [**Python**](https://www.python.org/) - A versatile and widely-used programming language that excels in various domains, including but not limited to, data analysis, visualization, artificial intelligence, and scripting.

### Libraries

- [**Matplotlib**](https://matplotlib.org/) - A comprehensive library for creating static, animated, and interactive visualizations in Python. It is used in this project to plot the growth of the investment over time, providing a clear and intuitive graphical representation of the data.

### Financial Calculations

- The `calculate_future_value` function embodies the financial logic behind the application. It utilizes the fundamental principles of compound interest to project the growth of an initial investment over time, factoring in the annual interest rate and the frequency of interest compounding.

### Data Visualization

- The `plot_investment_growth` function leverages Matplotlib to create insightful plots. It visualizes the progression of the investment's future value over the specified number of years, offering a visual aid to better understand the impact of time and compounding frequency on the investment.

### Development Tools

- [**Git**](https://git-scm.com/) - Used for version control to track and manage changes to the project codebase.
- [**GitHub**](https://github.com/) - Hosts the repository and facilitates collaboration, issue tracking, and code review.

### Integrated Development Environment (IDE)

- [**PyCharm**](https://www.jetbrains.com/pycharm/) / [**Visual Studio Code**](https://code.visualstudio.com/) - These IDEs are recommended for developing Python applications due to their robust support for Python code, debugging capabilities, and extensive plugin ecosystems.

### Execution Environment

- [**Local Python Environment**](https://docs.python.org/3/tutorial/venv.html) - It is suggested to use a virtual environment for Python to isolate project dependencies and manage libraries specific to this project.

### Additional Tools

- [**PIP**](https://pypi.org/project/pip/) - The package installer for Python, used to install Matplotlib and any other dependencies that may be required.

### Documentation

- [**Docstrings**](https://www.python.org/dev/peps/pep-0257/) - The project uses docstrings following the PEP 257 convention to provide documentation for each function within the code.

This "Built With" section serves as a comprehensive guide to the environment and tools necessary to run, develop, and contribute to the project. It ensures that developers can replicate the development environment and understand the dependencies and tools at the core of the project's functionality.

## Getting Started

This section will guide you through setting up your local environment to run the investment growth calculation and visualization script. Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following software installed on your computer:

- Python (3.x or later)
- pip (Python package installer)
- Git (Version control system)

### Installation

1. **Clone the repository**
   - Open your terminal and clone the repository using Git:
     ```sh
     git clone https://github.com/your-username/your-repository-name.git
     ```
   - Navigate to the cloned directory:
     ```sh
     cd your-repository-name
     ```

2. **Set up a virtual environment (Optional but recommended)**
   - Create a virtual environment to manage dependencies for the project:
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```sh
       venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```sh
       source venv/bin/activate
       ```

3. **Install dependencies**
   - Install the required packages using pip:
     ```sh
     pip install matplotlib
     ```

### Running the Script

- With the dependencies installed, you can run the script using Python:
  ```sh
  python script_name.py
  ```
  Replace `script_name.py` with the actual name of your Python script.

### Usage

To use the script with your own data, modify the `present_value`, `annual_interest_rate`, `investment_period_years`, and `compoundings_per_year` variables in the example usage section of the script.

```python
# Example usage - Modify these values as needed
present_value = 10000  # Your initial investment amount
annual_interest_rate = 0.05  # Your annual interest rate as a decimal
investment_period_years = 10  # Your investment period in years
compoundings_per_year = 4  # Your compounding frequency per year
```

After setting your own values, run the script again to see the new results.

### Testing

- You can test the functions in the script to ensure they're calculating values correctly. Consider writing unit tests using a framework like `unittest` that comes with Python.

### Contributing

If you would like to contribute to the project, please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

### Troubleshooting

If you encounter any issues:

- Make sure all the prerequisite software is installed and up to date.
- Check that you have activated the virtual environment before installing dependencies.
- Verify that you are using the correct versions of Python and pip by running `python --version` and `pip --version`.

### Support

For additional help or feedback, please file an issue in the GitHub repository, detailing the problem and steps to reproduce it, if applicable.

## Roadmap

See the [open issues](https://github.com//Future-Value-Of-A-Single-Sum/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Future-Value-Of-A-Single-Sum/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Future-Value-Of-A-Single-Sum/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Future-Value-Of-A-Single-Sum/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
