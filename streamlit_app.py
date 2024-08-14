import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import io
import altair as alt
import pydeck as pdk

# Read and process data. 
def load_data(file):
    data = pd.read_csv(file)            
    return data

# Analyze and visualize data. 
def analyze_data(data):
    import streamlit as st
    st.title("Data Collection")
    st.write("""This is the dataset is  the California Housing Data in Kaggle used in the paper by Pace, R. Kelley, and Ronald Barry. "Sparse spatial autoregressions." Statistics & Probability Letters 33.3 (1997): 291-297.. 
            It serves as an excellent introduction to implementing machine learning algorithms because it requires rudimentary data cleaning, has an easily understandable list of variables and sits at an optimal size between being too toyish and too cumbersome.
            The data contains information from the 1990 California census. So although it may not help you with predicting current housing prices like the Zillow Zestimate dataset, it does provide an accessible introductory dataset for teaching people about the basics of machine learning.
            The data pertains to the houses found in a given California district and some summary stats about them based on the 1990 census data. The columns are as follows, their names are pretty self-explanatory:
            """)
    st.image("https://th.bing.com/th/id/OIP.AVNkZ2r3O5as_sFJYwYhvQHaEX?w=1600&h=942&rs=1&pid=ImgDetMain", caption="California Housing Data ")


    st.title(" Data information :house:")
    st.write(data.describe())
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue() 
    st.text(s)
    st.markdown("***1. Median House Value***: Median house value for households within a block (measured in US Dollars) :gray[$]:")
    st.markdown("***2. Median Income***: Median income for households within a block of houses (measured in tens of thousands of US Dollars) :gray[10k$]:")
    st.markdown("***3. Median Age***: Median age of a house within a block; a lower number is a newer building :gray:[years]:")
    st.markdown("***4. Total Rooms***: Total number of rooms within a block")    
    st.markdown("***5. Total Bedrooms***: Total number of bedrooms within a block")
    st.markdown("***6. Population***: Total number of people residing within a block")
    st.markdown("***7. Households***: Total number of households, a group of people residing within a home unit, for a block")
    st.markdown("***8. Latitude***: A measure of how far north a house is; a higher value is farther north :gray[°]:")   
    st.markdown("***9. Longitude***: A measure of how far west a house is; a higher value is farther west :gray[°]:")
    st.markdown("***10. Distance to coast***: Distance to the nearest coast point :gray[m]:")   
    st.markdown("***11. Distance to Los Angeles***: Distance to the centre of Los Angeles :gray[m]:")
    st.markdown("***12. Distance to San Diego***: Distance to the centre of San Diego :gray[m]:")   
    st.markdown("***13. Distance to San Jose***: Distance to the centre of San Jose :gray[m]:")
    st.markdown("***14. Distance to San Francisco***: Distance to the centre of San Francisco :gray[m]:") 

    st.title("Data Processing :mag:")
    st.header("1. Check for null values",divider=True)
    st.write(data.isnull().sum())
  
    data=data.dropna() # Delete lines that contain nulls
    st.header(" Check for null values ​​after deletion :white_check_mark:")   
    st.write(data.isnull().sum())

    st.header("2. Check for duplicate records",divider=True)
    st.write(f"Number of duplicate records: {data.duplicated().sum()}")
    data[data.duplicated()]

    data=data.drop_duplicates() 
    st.header("Check records after removing duplicates :white_check_mark:")
    st.write(f"Number of duplicate records: {data.duplicated().sum()}")
    data[data.duplicated()]


    st.title("Data Visualization :bar_chart:")
    st.header("1. Average home value distribution chart",divider=True)
    fig, ax = plt.subplots()
    sns.histplot(data['Median_House_Value'], bins=50, kde=True, ax=ax)
    st.pyplot(fig)
    st.write("""The distribution plot shows that the median value of the homes in the dataset is clearly concentrated at low values,
               with a large number of homes having median values ​​ranging from $50,000 to $200,000.
            The distribution is skewed to the right, with a small number of homes having very high median values, up to around $500,000 or more.""")

# Statistical calculations
    mean, median, std_dev = calculate_statistics(data, 'Median_House_Value')
    st.write(f"Mean value of Median_House_Value: {mean}")
    st.write(f"Median value of Median_House_Value: {median}")
    st.write(f"standard deviation value of Median_House_Value: {std_dev}")

# Draw line graph
    st.header("2. The graph shows the average value versus the average age of the homes",divider=True)
    st.write("""This line plot illustrates the variation in average median house values across median age groups. 
             It shows the trend of increasing or decreasing house values as the median age of the area changes.
            Line plots are useful for identifying trends and fluctuations in data over time or across other variables.""")
    median_house_values = data.groupby('Median_Age')['Median_House_Value'].mean().reset_index()
    plot_line(median_house_values, 'Median_Age', 'Median_House_Value')
    st.write("""The graph shows the relationship between the average age of homes and their average value. 
             There is a trend for home values ​​to change as the average age of the area increases, suggesting that the age of homes has a significant impact on their market value.""")
    
    # Use functions to calculate and draw graphs
    st.header("3. Home Value Chart Based on Distance to City",divider=True)
    st.write("""This pie chart visualizes the average median house value based on distances to key cities 
             (Coast, LA, San Diego, San Jose, San Francisco). Each slice represents a city, 
             and its area corresponds to the percentage of average house prices near that city relative to the others.""")
    avg_values = avg_house_value_by_distance(data)
    cities = ['Distance_to_coast', 'Distance_to_LA', 'Distance_to_SanDiego', 'Distance_to_SanJose', 'Distance_to_SanFrancisco']
    plot_pie_chart(avg_values, cities)
    st.write("This pie chart clearly shows the difference in median home values ​​based on distance to major cities. ")
    st.write("The results from the chart can help investors and market analysts make more informed decisions about investing in specific areas.")
    
# Draw bubble chart
    st.header("4. Bubble Chart of Median_Income vs Median_House_Value with Bubble Size Representing Population",divider=True)
    st.write("""The bubble chart uses the Altair library to visualize the relationship between median income (Median_Income), median house value (Median_House_Value), 
             and population (Population). In the chart, the X-axis represents income, the Y-axis represents house value, and the bubble size reflects population size. 
             This chart helps identify trends and prominent areas in real estate data.""")
    plot_bubble_chart_altair(data, 'Median_Income', 'Median_House_Value', 'Population')
    st.write("Positive Correlation: The chart may show a positive correlation between income and home value, meaning that as income increases, home value tends to increase.")
    st.write("Hot Areas: Areas with large bubbles but not too high home values ​​may be places with great potential for real estate development.")
   
    
    plot_combined_distance_map(data)
    st.write("""The distance combination chart provides a better understanding of the relationship between home values ​​and distance to major cities, 
             providing a powerful tool for investment decision making and real estate market analysis. Analyzing data from multiple distances provides 
             a comprehensive view of home value trends and assists in real estate development planning.""")
 
# Function to plot maps with multiple distance variables
def plot_combined_distance_map(data):
    # Ensure columns are numeric
    distance_columns = [
        'Distance_to_coast', 
        'Distance_to_LA', 
        'Distance_to_SanDiego', 
        'Distance_to_SanJose', 
        'Distance_to_SanFrancisco'
    ]
    
    # Convert columns to numeric
    for col in distance_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with NaN values in distance columns
    data = data.dropna(subset=distance_columns)
    
    # Normalize distance columns for combined visualization
    for col in distance_columns:
        data[f'{col}_norm'] = data[col] / data[col].max()

    # Combine all distance data into a single DataFrame for plotting
    combined_data = data[['Latitude', 'Longitude'] + [f'{col}_norm' for col in distance_columns]]
    
    # Plotting the map
    st.header("5. Combined Map of Median House Values by Distance to Major Cities",divider=True)
    st.write("""The map chart combining median home value by distance to major cities provides
              an overview of the distribution of median home value based on distance to major cities such as the Coast, 
             LA, San Diego, San Jose, and San Francisco. The chart uses the HexagonLayer and ScatterplotLayer layers to show how home value changes with distance from major cities. 
             Each distance is normalized and displayed on the same map, with color and point size representing the distribution of home value by distance from major cities.""")
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=data['Latitude'].mean(),
                longitude=data['Longitude'].mean(),
                zoom=7,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=combined_data,
                    get_position="[Longitude, Latitude]",
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                    get_fill_color="[255 * (Distance_to_coast_norm + Distance_to_LA_norm + Distance_to_SanDiego_norm + Distance_to_SanJose_norm + Distance_to_SanFrancisco_norm) / 5, 0, 0, 160]"
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=combined_data,
                    get_position="[Longitude, Latitude]",
                    get_color="[200, 30, 0, 160]",
                    get_radius=200,
                ),
            ],
        )
    )


# Function to draw bubble chart using Altair
def plot_bubble_chart_altair(data, x_column, y_column, size_column):
    chart_data = data[[x_column, y_column, size_column]]
    c = alt.Chart(chart_data).mark_circle().encode(
        x=x_column,
        y=y_column,
        size=size_column,
        color=y_column,
        tooltip=[x_column, y_column, size_column]
    )
    st.altair_chart(c, use_container_width=True)

# The function calculates the average house value according to each distance
def avg_house_value_by_distance(data):
    avg_house_value = []
    avg_house_value.append(data['Median_House_Value'][data['Distance_to_coast'] == data['Distance_to_coast'].min()].mean())
    avg_house_value.append(data['Median_House_Value'][data['Distance_to_LA'] == data['Distance_to_LA'].min()].mean())
    avg_house_value.append(data['Median_House_Value'][data['Distance_to_SanDiego'] == data['Distance_to_SanDiego'].min()].mean())
    avg_house_value.append(data['Median_House_Value'][data['Distance_to_SanJose'] == data['Distance_to_SanJose'].min()].mean())
    avg_house_value.append(data['Median_House_Value'][data['Distance_to_SanFrancisco'] == data['Distance_to_SanFrancisco'].min()].mean())
    return avg_house_value

import matplotlib.pyplot as plt
# Function to draw a pie chart
def plot_pie_chart(values, labels):
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Average Median House Value by Distance to Cities')
    plt.axis('equal')  # Assurez-vous que le graphique dessine un cercle
    st.pyplot(plt)


# Calculated statistics
def calculate_statistics(data, column):
    mean = data[column].mean()
    median = data[column].median()
    std_dev = data[column].std()
    return mean, median, std_dev

# Line chart function
def plot_line(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_column], data[y_column], marker='o', linestyle='-', color='b', label=y_column)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Line Plot of {y_column} over {x_column}')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)



# Save analysis results
def save_analysis_results(data, filename):
    data.to_csv(filename, index=False)
    st.write(f"The analysis results have been saved. {filename}")

# Streamlit User Interface
def main():
    st.title("California Housing Data Analytics Tool")

    uploaded_file = st.file_uploader("Select the CSV file containing the data", type="csv")
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write("Data has been uploaded successfully")

        if st.button("Data Analysis"):
            analyze_data(data)
        
        if st.button("Save analysis results"):
            save_analysis_results(data, "analysis_results.csv")

if __name__ == "__main__":
    main()



# st.title('Hello, Streamlit!')
# st.write("This is a simple example to demonstrate Streamlit's capabilities.")

#>streamlit run House.py
