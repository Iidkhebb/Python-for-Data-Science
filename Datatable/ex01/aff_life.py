import matplotlib.pyplot as plt
from load_csv import load

def plot_life_expectancy(country_name, df):
    # Filter data for the specified country
    country_data = df[df['country'] == country_name]

    # Get the years (column names)
    years = country_data.columns[1:]  # Assuming the first column is 'country'

    # Extract life expectancy values for the country
    life_expectancy = country_data.iloc[0, 1:]  # Assuming the first row is the country
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(years, life_expectancy, label=country_name)
    
    # Add title and labels
    plt.title(f'Life Expectancy Over Time in {country_name}')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (Years)')
    
    # Show legend
    plt.legend()
    
    # Customize x-axis to show fewer years
    num_ticks = 10  # Number of ticks you want to display
    tick_positions = list(range(0, len(years), max(len(years) // num_ticks, 1)))
    tick_labels = [years[i] for i in tick_positions]
    plt.xticks(tick_positions, tick_labels, rotation=45)
    
    # Show plot
    plt.grid(True)

    plt.show()

def main():
    # Load the CSV file
    df = load("life_expectancy_years.csv")
    
    # Check if data is loaded successfully
    if df is not None:
        # Country name for the campus
        campus_country = "France"  # Replace with your campus country
        
        # Plot life expectancy for the campus country
        plot_life_expectancy(campus_country, df)
    else:
        print("Failed to load data. Exiting program.")

if __name__ == "__main__":
    main()
