import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set global aesthetic
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (12, 6)

def run_amazon_pipeline(file_path):
    print(">>> Initializing Advanced Sales Pipeline...")
    
    # 1. LOAD & DEBUG COLUMNS
    df = pd.read_csv(file_path, low_memory=False)
    df.columns = df.columns.str.strip() # Remove hidden spaces
    cols = list(df.columns)
    
    # 2. DYNAMIC MAPPING (Fixes 'KeyError' issues)
    # This automatically finds the right columns even if names vary
    target_amt = next((c for c in ['Amount', 'PurchaseAmount', 'Sales'] if c in cols), None)
    target_date = next((c for c in ['Date', 'PurchaseDate', 'Order Date'] if c in cols), None)
    target_cat = next((c for c in ['Category', 'Product', 'Item'] if c in cols), None)
    
    print(f"Mapped Columns: Date->{target_date}, Amount->{target_amt}, Category->{target_cat}")

    # 3. DATA REFINEMENT
    if target_date:
        df[target_date] = pd.to_datetime(df[target_date], errors='coerce')
    if target_amt:
        df[target_amt] = pd.to_numeric(df[target_amt], errors='coerce').fillna(0)
        # Statistical Outlier Removal (IQR Method)
        q1, q3 = df[target_amt].quantile([0.25, 0.75])
        iqr = q3 - q1
        df = df[(df[target_amt] >= q1 - 1.5*iqr) & (df[target_amt] <= q3 + 1.5*iqr)]

    # =========================================================
    # 6 ADVANCED VISUALIZATIONS
    # =========================================================
    print("\n>>> Generating Technical Visuals...")

    # 1. TIME-SERIES MOMENTUM (Line + Moving Average)
    # Proves the "Growth Trend" by smoothing out daily noise
    plt.figure()
    daily_sales = df.groupby(target_date)[target_amt].sum()
    daily_sales.plot(alpha=0.3, label='Daily Sales')
    daily_sales.rolling(window=7).mean().plot(color='red', lw=2, label='7-Day Moving Avg')
    plt.title('1. Sales Momentum & Moving Average Trend', fontsize=14)
    plt.legend()
    plt.show()

    # 2. HEXBIN DENSITY (Quantity vs Amount)
    # Useful for finding the "Price Sweet Spot" in large datasets
    target_qty = next((c for c in ['Qty', 'Quantity'] if c in cols), None)
    if target_qty and target_amt:
        plt.figure()
        plt.hexbin(df[target_qty], df[target_amt], gridsize=20, cmap='YlGnBu')
        plt.colorbar(label='Frequency')
        plt.xlabel('Quantity Ordered')
        plt.ylabel('Transaction Value')
        plt.title('2. Transaction Density: Quantity vs Value', fontsize=14)
        plt.show()

    # 3. KERNEL DENSITY ESTIMATE (KDE) - Sales Distribution
    # Shows the statistical "probability" of a specific price point
    plt.figure()
    sns.kdeplot(df[target_amt], fill=True, color="teal", bw_adjust=0.5)
    plt.title('3. Probability Density: Distribution of Sales Value', fontsize=14)
    plt.show()

    # 4. PARETO BAR CHART (Top Categories)
    # Identifies the 20% of products driving 80% of revenue
    if target_cat:
        plt.figure()
        cat_sales = df.groupby(target_cat)[target_amt].sum().sort_values(ascending=False).head(10)
        sns.barplot(x=cat_sales.values, y=cat_sales.index, palette='rocket')
        plt.title('4. Revenue Champions: Top 10 Product Categories', fontsize=14)
        plt.show()

    # 5. BOXEN PLOT (Advanced Variance Analysis)
    # Better than a boxplot for large data to show "heavy tails"
    status_col = next((c for c in ['Status', 'Ship-Service-Level'] if c in cols), None)
    if status_col:
        plt.figure()
        sns.boxenplot(data=df, x=status_col, y=target_amt, palette='Set2')
        plt.xticks(rotation=45)
        plt.title('5. Value Distribution by Order Status', fontsize=14)
        plt.show()

    # 6. CORRELATION HEATMAP (Numeric Dependencies)
    # Mathematically proves which variables influence each other
    plt.figure()
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('6. Multivariate Correlation Matrix', fontsize=14)
    plt.show()

if __name__ == "__main__":
    PATH = '/Users/sneha/Documents/Projects/Amazon Sales/Amazon Sale Report.csv'
    try:
        run_amazon_pipeline(PATH)
        print("\n>>> Pipeline Completed Successfully.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR]: {e}")