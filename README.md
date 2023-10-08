# Page-Visits-Funnel
This exercise is included in the [Codecademy.com Learn Data Analysis with Pandas](https://www.codecademy.com/enrolled/courses/data-processing-pandas) course. You may find my certificate of completion on my [LinkedIn page](https://www.linkedin.com/in/nick-m-doyle/).

📣 The source data from Codecadamy contains four csv files: `visits`, `cart`, `checkout`, and `purchase`. As I was working through this miniature project, I noticed that the data did not make sense for two main reasons:
- `purchase.csv` contained more rows than `checkout`. This doesn't make sense because the data is supposed to become smaller and smaller (like a *funnel*) with each step in the process.
- The `all_data` DataFrame near the end of the module contained more rows (2108) than the `visits` DataFrame. This doesn't make sense because `visits` should contain the 100% of the rows (2000 rows)
Once I realized this, I began troubleshooting:
1. First, I re-reviewed my code to see if I had done something wrong (E.g., an incorrect join, referenced the wrong variable).
2. Second, I reviewed the data in Excel to see the correct counts. I loaded each file into a distinct workbook, defined them as tables, loaded the tables into PowerQuery, and did Left Join merges to produce the same data as what was in the `all_data` DataFrame, but with one table at a time. Doing this step-by-step pinpointed the offending dataset: `purchases`.
3. Third, I took a closer look at the dataset. It contained duplicate rows in the `user` column. Doing a Left Join between `checkout` and `purchase` on `user` was creating additional rows because there were multiple matches.

In the context of the exercise, I created a copy of the `checkout.csv` file, and removed the duplicates and also deleted random rows. This was in hopes to simulate what the original dataset intended to do. I saved this file as `adj_purchase.csv`, included it in the project files (keeping the original `purchases.csv` dataset as well, for reference), and simply updated the code read the new file instead. 

This exercise demonstrates the following skills:
1. **Data Import and Reading**: This demonstrates that I can import data from CSV files using the pandas library, specifying date columns to be parsed as datetime objects.
2. **Data Exploration and Display**: This demonstrates an initial exploration of data by displays the first few rows of each DataFrame ('visits', 'cart', 'checkout', 'purchase') to get an initial understanding of the data.
3. **Data Analysis and Calculation**: The code calculates various metrics such as the total number of visits, carts, checkouts, and purchases. It also calculates the percentage of users who performed certain actions (e.g., added to cart but didn't checkout).
4. **Data Merging and Joining**: This demonstrates my ability to merge DataFrames using the pd.merge() function to combine data from different sources.
5. **Data Cleaning and Transformation**: The code considers null values in the merged 'all_data' DataFrame. I also calculate percentages of users who *didn't* perform certain actions.
6. Time Series Analysis: The coder calculates the time it took for users to make a purchase after visiting the site by subtracting 'visit_time' from 'purchase_time'. This demonstrates the ability to work with time series data.
7. Data Visualization: Since the matplotlib library doesn't have funnel charts, I use the Plotly library instead to create a simple visualization representitive of the project. I customized the chart using colors, size, and label positions.

You will find notes explaining my thought processes within the included Jupyter notebook file.

