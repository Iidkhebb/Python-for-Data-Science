import matplotlib.pyplot as plt
from load_csv import load


def plot_population_comparison(
    country1_data, country1_name, country2_data, country2_name
):

    years = range(1800, 2051)
    country1_population = (
        country1_data.iloc[:, 1:252]
        .apply(lambda x: x.str.replace("M", "").astype(float))
        .values.flatten()
    )  # Convert to numerical values
    country2_population = (
        country2_data.iloc[:, 1:252]
        .apply(lambda x: x.str.replace("M", "").astype(float))
        .values.flatten()
    )  # Convert to numerical values

    max_population = max(country1_population.max(), country2_population.max())
    ylim_max = max_population * 1.1
    plt.plot(years, country1_population, label=country1_name)
    plt.plot(years, country2_population, label=country2_name)

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(
        "Population Comparison: " + country1_name + " vs " + country2_name
    )
    plt.ylim(
        0, ylim_max
    )  # Set y-axis limits to show range from 0 to 60 million

    plt.grid(True)

    plt.legend(loc="lower right")
    plt.show()


def main():
    # Load population data
    population_data = load("population_total.csv")

    # Filter data for your campus
    # (replace 'Your Campus' with the name of your campus)
    your_campus_data = population_data[population_data["country"] == "France"]

    # Choose another country for comparison
    # (replace 'Other Country' with the name of the country you choose)
    other_country_data = population_data[
        population_data["country"] == "Belgium"
    ]

    # Plot population comparison
    plot_population_comparison(
        your_campus_data, "France", other_country_data, "Belgium"
    )


if __name__ == "__main__":
    main()
