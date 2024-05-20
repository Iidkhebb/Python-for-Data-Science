import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def projection(income_data, life_expectancy_data):
    # Selecting data for the year 1900
    income_1900 = income_data[["country", "1900"]]
    life_expectancy_1900 = life_expectancy_data[["country", "1900"]]

    # Renaming columns for clarity
    income_1900.columns = ["country", "income_1900"]
    life_expectancy_1900.columns = ["country", "life_expectancy_1900"]

    # Merging data on 'country' to get GDP per capita
    # and life expectancy for the same countries
    merged_data = pd.merge(income_1900, life_expectancy_1900, on="country")

    # Plotting
    plt.figure(figsize=(14, 8))
    plt.scatter(
        merged_data["income_1900"],
        merged_data["life_expectancy_1900"],
        label="1900",
    )
    plt.title("Life Expectancy vs. Gross National Product (1900)")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_data = load("life_expectancy_years.csv")
    projection(income_data, life_expectancy_data)


if __name__ == "__main__":
    main()
