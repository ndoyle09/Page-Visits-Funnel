# Page-Visits-Tunnel
This exercise is included in the [Codecademy.com Learn Data Analysis with Pandas](https://www.codecademy.com/enrolled/courses/data-processing-pandas) course. You may find my certificate of completion on my [LinkedIn page](https://www.linkedin.com/in/nick-m-doyle/).

This exercise demonstrates the following skills:
1. **Data Import and Reading**: This demonstrates that I can import data from CSV files using the pandas library, specifying date columns to be parsed as datetime objects.
2. **Data Exploration and Display**: This demonstrates an initial exploration of data by displays the first few rows of each DataFrame ('visits', 'cart', 'checkout', 'purchase') to get an initial understanding of the data.
3. **Data Analysis and Calculation**: The code calculates various metrics such as the total number of visits, carts, checkouts, and purchases. It also calculates the percentage of users who performed certain actions (e.g., added to cart but didn't checkout).
4. **Data Merging and Joining**: This demonstrates my ability to merge DataFrames using the pd.merge() function to combine data from different sources.
5. **Data Cleaning and Transformation**: The code considers null values in the merged 'all_data' DataFrame. I also calculate percentages of users who *didn't* perform certain actions.
6. Time Series Analysis: The coder calculates the time it took for users to make a purchase after visiting the site by subtracting 'visit_time' from 'purchase_time'. This demonstrates the ability to work with time series data.
7. Data Visualization: Since the matplotlib library doesn't have funnel charts, I use the Plotly library instead to create a simple visualization representitive of the project. I customized the chart using colors, size, and label positions.

You will find notes explaining my thought processes within the included Jupyter notebook file.

