import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Function to read the dataset and preprocess
def read_and_preprocess(file_path):
    weather_data = pd.read_csv(file_path)
    weather_data['time'] = pd.to_datetime(weather_data['time'])
    weather_data.set_index('time', inplace=True)
    weather_data['Ftemp'] = (weather_data['Ktemp'] - 273.15) * 9/5 + 32
    return weather_data

# Function to plot the graph
def plot_graph(year, weather_data):
    plt.close('all')  # Close previous plots to prevent memory leak
    fig, ax = plt.subplots(figsize=(10, 5))
    year_data = weather_data[weather_data.index.year == year]
    monthly_avg_temp = year_data.groupby(year_data.index.month)['Ftemp'].mean()
    ax.scatter(monthly_avg_temp.index, monthly_avg_temp.values)  # Changed to scatter plot here
    ax.set_title(f'Average Monthly Temperature in {year}')
    ax.set_xlabel('Month')
    ax.set_xticks(range(1, 13))  # Set x-ticks to show all months
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.set_ylabel('Average Temperature (°F)')
    ax.grid(True)
    return fig

# Streamlit app
def main():
    st.title("Weather Visualization")

    # Assuming 'weather.csv' is your file path
    file_path = 'weather.csv'  # replace with the path to your CSV file
    weather_data = read_and_preprocess(file_path)

    # Slider for selecting the year
    years = weather_data.index.year.unique()
    year = st.slider('Select Year:', min_value=int(min(years)), max_value=int(max(years)), step=1)

    # Plotting
    fig = plot_graph(year, weather_data)
    st.pyplot(fig)

if __name__ == "__main__":
    main()