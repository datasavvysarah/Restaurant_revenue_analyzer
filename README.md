## Overview

This project provides comprehensive analysis of sales data using Python, focusing on key business metrics and trends. The analysis covers revenue patterns, product performance, customer behavior, and statistical insights to support data-driven business decisions.

## Project Description

The Restaurant Data Analysis Project processes raw sales transaction data to answer critical business questions through statistical analysis and data visualization. The project transforms raw CSV data into actionable insights using pandas for data manipulation, matplotlib and seaborn for visualizations, and numpy for statistical calculations.

## Dataset

The analysis uses sales transaction data containing:
- **Order ID**: Unique transaction identifiers
- **Date**: Transaction dates
- **Product**: Product names
- **Price**: Unit prices
- **Quantity**: Units sold per transaction
- **Purchase Type**: Type of purchase
- **Payment Method**: Payment methods used
- **Manager**: Sales manager information
- **City**: Transaction locations

## Key Analysis Questions Answered

The project addresses 10 fundamental business questions:

1. **What was the Most Preferred Payment Method?**
2. **Which Product was the Most Selling by Quantity and Revenue?**
3. **Which City had Maximum Revenue, and Which Manager Earned Maximum Revenue?**
4. **What was the Average Revenue?**
5. **What was the Average Revenue of November & December?**
6. **What was the Standard Deviation of Revenue and Quantity?**
7. **What was the Variance of Revenue and Quantity?**
8. **Was Revenue Increasing or Decreasing Over Time?**
9. **What was the Average Quantity Sold & Average Revenue for Each Product?**
10. **What was the Total Number of Orders/Sales Made?**

## Features

### Data Processing
- **Data Cleaning**: Handles missing values, duplicates, and data type conversions
- **Revenue Calculation**: Computes revenue from quantity and price data
- **Date Processing**: Converts dates for time-series analysis
- **Statistical Analysis**: Calculates descriptive statistics, variance, and standard deviation

### Visualizations
- **Trend Analysis**: Time-series plots showing revenue trends with correlation analysis
- **Comparative Charts**: Bar charts comparing performance across categories
- **Distribution Analysis**: Histograms and distribution plots
- **Dashboard Views**: Multi-panel visualizations for comprehensive insights
- **Interactive Elements**: Moving averages and trend lines

### Statistical Insights
- **Correlation Analysis**: Measures trend strength using correlation coefficients
- **Variance Analysis**: Quantifies data variability
- **Growth Rate Calculations**: Month-over-month and period comparisons
- **Outlier Detection**: Identifies unusual patterns in the data

## Technologies Used

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **numpy**: Numerical computations
- **datetime**: Date and time processing

## File Structure

```
restaurant_revenue_analyzer/
│
|── README.md                          # Project documentation
├── Python_SalesData.xlsx - Raw.csv    # Raw sales data
├── sales_analysis.ipynb               # Jupyter notebook with analysis
├── analysis.py                        # Python script version
```

## Installation

1. Clone or download the project files
2. Install required dependencies:
```bash
pip install pandas matplotlib seaborn numpy
```

## Usage

### Running the Analysis

1. **Jupyter Notebook**: Open `analysis.ipynb` in Jupyter Notebook or JupyterLab
2. **Python Script**: Run `python analysis.py` from the command line

### Data Input
- Place your sales data CSV file in the project directory
- Update the file path in the code if necessary
- Ensure your data contains the required columns

### Output
- **Console Output**: Detailed statistical summaries and insights
- **Visualizations**: Multiple charts and graphs
- **Dashboard**: Comprehensive visual analysis panels

## Key Findings Format

Each analysis section provides:
- **Quantitative Results**: Specific numbers and percentages
- **Business Interpretation**: What the results mean for the business
- **Visual Confirmation**: Charts supporting the findings
- **Trend Analysis**: Direction and strength of patterns
- **Comparative Insights**: Rankings and performance comparisons

## Visualization Types

- **Line Charts**: Revenue trends over time
- **Bar Charts**: Category comparisons
- **Histograms**: Distribution analysis
- **Scatter Plots**: Correlation analysis
- **Multi-panel Dashboards**: Comprehensive overviews
- **Moving Averages**: Smoothed trend analysis

## Statistical Methods

- **Descriptive Statistics**: Mean, median, standard deviation
- **Correlation Analysis**: Pearson correlation coefficients
- **Variance Analysis**: Data spread measurement
- **Trend Detection**: Linear regression and correlation
- **Growth Rate Calculation**: Period-over-period changes
- **Outlier Detection**: IQR-based anomaly identification

## Customization

The code can be easily adapted for different datasets by:
- Modifying column names in the data processing section
- Adjusting date formats and parsing
- Customizing visualization colors and styles
- Adding new analysis questions
- Modifying statistical calculations

## Business Applications

This analysis framework is suitable for:
- **Retail Sales Analysis**
- **E-commerce Performance Tracking**
- **Regional Sales Comparison**
- **Product Performance Evaluation**
- **Seasonal Trend Analysis**
- **Manager Performance Assessment**

## Requirements

- Python 3.6+
- pandas >= 1.0.0
- matplotlib >= 3.0.0
- seaborn >= 0.11.0
- numpy >= 1.18.0

## Contributing

To extend this analysis:
1. Fork the project
2. Add new analysis functions
3. Include corresponding visualizations
4. Update documentation
5. Test with sample data

## License

This project is available for educational and commercial use.

## Author

I created this as part of my data analysis portfolio demonstrating Python proficiency in data science, statistical analysis, and business intelligence visualization.

---

**Note**: This project demonstrates practical application of data science techniques for business analytics, showcasing skills in data cleaning, statistical analysis, and data visualization using Python.
