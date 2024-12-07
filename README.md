Amazon Sales Analysis
This project performs a detailed analysis of an Amazon sales dataset, focusing on cleaning, exploratory data analysis (EDA), and visualization. It identifies trends, customer purchasing behavior, and key insights from the sales data.

Features:
Data Cleaning:
Handles missing values:
Replaces missing Age values with the median.
Fills missing Gender values with "Unknown."
Imputes missing PurchaseAmount values with the median.
Standardizes Gender values (M -> Male, F -> Female).
Converts PurchaseDate to a datetime format for time-based analysis.
Removes duplicate records.
Detects and removes outliers in PurchaseAmount using the Interquartile Range (IQR) method.

Exploratory Data Analysis (EDA):
Age Distribution:
A histogram with a kernel density estimate (KDE) is used to visualize the distribution of customer ages.

Gender Distribution:
A pie chart shows the proportion of male, female, and unknown customers.

Top 10 Customers:
A bar chart highlights the top 10 customers based on their total purchase amounts.

Monthly Purchase Trends:
A line chart tracks purchase trends over time, aggregated by month.
Correlation Heatmap:
A heatmap reveals the relationships between numerical variables like Age and PurchaseAmount.

Visualizations:
Uses Seaborn and Matplotlib to generate informative and appealing plots.
Visualizations include histograms, pie charts, bar charts, line charts, and heatmaps.
