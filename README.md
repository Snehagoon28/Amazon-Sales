📦 Amazon Sales Intelligence & Predictive Analytics
📌 Project Overview
This project provides a high-level analytical deep-dive into Amazon sales data. By moving beyond basic reporting, this pipeline implements statistical smoothing, density-based profiling, and multivariate correlation to uncover hidden patterns in transaction volumes, customer behavior, and revenue drivers.

🧠 Business Logic & Problem Statement
Standard e-commerce reports are often cluttered with outliers and daily fluctuations that mask the true health of a business. This project solves the "Signal vs. Noise" problem by applying statistical filters. It answers critical business questions:
1. What is our actual sales momentum when adjusted for volatility?
2. Which price points have the highest transaction density?
3. Are there significant correlations between quantity ordered and status updates?

The code features a Dynamic Column Mapper, making it compatible with various Amazon Seller Report formats by automatically identifying core features like Date, Amount, and Category.

🛠️ Technical Features
- Dynamic Data Engineering: Automated column detection and cleaning that handles varied CSV headers and trailing whitespaces.
- Statistical Refinement: Implementation of the IQR (Interquartile Range) Method to filter out financial outliers and provide a realistic view of core business performance.
- Time-Series Smoothing: Utilization of 7-Day Moving Averages to eliminate daily "noise" and identify true market momentum.
- Density Profiling: Application of Hexbin mapping and Kernel Density Estimation (KDE) to analyze transaction concentrations.

📊 Visual Intelligence Suite
- The pipeline generates 6 technically rigorous visualizations designed for business decision-making:
- Sales Momentum Trend: Daily revenue vs. 7-Day Moving Average to track growth trajectories.
- Transaction Density (Hexbin): Mapping Quantity vs. Value to identify the "pricing sweet spot."
- Probability Density (KDE): A smooth statistical distribution of transaction values.
- Pareto Category Analysis: Identifying the top 10 product categories driving the bulk of revenue.
- Boxen Plot Variance: Advanced variance analysis of order values categorized by shipping or order status.
- Multivariate Correlation: A mathematical matrix proving dependencies between numeric variables.

🤝 Contributing
Contributions are welcome! If you have ideas for adding predictive forecasting (ARIMA/Prophet) to this pipeline, feel free to fork and submit a PR.
Visualizations include histograms, pie charts, bar charts, line charts, and heatmaps.
