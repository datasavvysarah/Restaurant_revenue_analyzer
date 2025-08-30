# %%
import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# %%
df = pd.read_csv(r'C:\Users\Sarah\OneDrive\Documenti\Axia Final Project\Python_SalesData.xlsx - Raw.csv', encoding='latin1')
df

# %%
df = df.rename(columns={
    'Unnamed: 1': 'Order ID',
    'Unnamed: 2': 'Date',
    'Unnamed: 3': 'Product',
    'Unnamed: 4': 'Price',
    'Unnamed: 5': 'Quantity',
    'Unnamed: 6': 'Purchase Type',
    'Unnamed: 7': 'Payment Method',
    'Unnamed: 8': 'Manager',
    'Unnamed: 9': 'City',
    'Unnamed: 0': 'NaN'
})
df

# %%
df = df.drop(df.index[0])
df

# %%
df = df.drop(columns=['NaN'])
df

# %%
df.info()

# %%
df = df.drop_duplicates(subset=['Order ID', 'Date', 'Product', 'Price', 'Quantity', 'Purchase Type', 'Payment Method', 'Manager', 'City'], keep='first')
df

# %%
df.describe()

# %%
import datetime as dt
import pandas as pd

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
df

# %%
df.info()

# %%
df['Order ID'] = df['Order ID'].astype(str).str.strip()
df['Order ID'] = df['Order ID'].str.strip('object')
df['Order ID'] = df['Order ID'].astype(int)
df['Price'] = df['Price'].astype(str).str.strip()
df['Price'] = df['Price'].astype(float)
df['Quantity'] = df['Quantity'].astype(str).str.strip()

# %%
df.info()

# %%
df['Quantity'] = df['Quantity'].astype(str).str.strip()
df['Quantity'] = df['Quantity'].astype(float)
df

# %%
df.info()

# %%
total_quantity = df['Quantity'].sum()
print(f"Total Quantity: {total_quantity}")


# %%
import datetime as dt
import pandas as pd

# 1. DESCRIPTIVE STATISTICS
print("=== DESCRIPTIVE STATISTICS ===")
print("\nOverall dataset info:")
print(df.info())

print("\nBasic statistics for numerical columns:")
print(df.describe())

print("\nQuantity statistics:")
print(f"Total Quantity: {df['Quantity'].sum()}")
print(f"Average Quantity: {df['Quantity'].mean():.2f}")
print(f"Median Quantity: {df['Quantity'].median():.2f}")
print(f"Standard Deviation: {df['Quantity'].std():.2f}")

# 2. DISTRIBUTIONS
print("\n=== DISTRIBUTIONS ===")
print("\nValue counts for categorical columns:")
for col in df.select_dtypes(include=['object']).columns:
    print(f"\n{col} distribution:")
    print(df[col].value_counts().head(10))

# 3. GROUP-WISE SUMMARIES
print("\n=== GROUP-WISE SUMMARIES ===")

# Group by categorical columns and sum quantities
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    print(f"\nQuantity by {col}:")
    summary = df.groupby(col)['Quantity'].agg(['count', 'sum', 'mean']).round(2)
    print(summary.head(10))
print("\n=== GROUP-WISE SUMMARIES ===")
print("\nQuantity by City:") 
df

# %%
## Time-based analysis if Date column exists
if 'Date' in df.columns:
    print("\n=== TIME-BASED TRENDS ===")
    
    # Convert Date back to datetime for analysis
    df['Date_temp'] = pd.to_datetime(df['Date'])
    
    # Monthly trends
    df['Month'] = df['Date_temp'].dt.to_period('M')
    monthly_summary = df.groupby('Month')['Quantity'].agg(['count', 'sum', 'mean']).round(2)
    print("\nMonthly quantity trends:")
    print(monthly_summary)

# %%
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Convert Object ID to int
df['Object ID'] = df['Object ID'].astype(int)

# Convert quantity with decimals to float
df['quantity'] = df['Quantity'].astype(float)



# %%
# Find the most preferred payment method
print("=== MOST PREFERRED PAYMENT METHOD ===\n")

# Get payment method counts
payment_counts = df['Payment Method'].value_counts()
print("Payment Method Usage:")
print(payment_counts)

# Find the most preferred (most frequent) payment method
most_preferred = payment_counts.index[0]
most_preferred_count = payment_counts.iloc[0]
total_transactions = len(df)
percentage = (most_preferred_count / total_transactions) * 100

print(f"\n ANSWER: The most preferred payment method is '{most_preferred}'")
print(f"   - Used in {most_preferred_count} transactions")
print(f"   - Represents {percentage:.1f}% of all transactions")

# Show percentage breakdown of all payment methods
print(f"\n Payment Method Breakdown:")
payment_percentages = (df['Payment Method'].value_counts() / len(df) * 100).round(1)
for method, pct in payment_percentages.items():
    print(f"   {method}: {pct}%")

# Visualize the data (optional)
print(f"\n Visual representation:")
for method, count in payment_counts.items():
    bar_length = int((count / payment_counts.max()) * 30)  # Scale to max 30 chars
    bar = "█" * bar_length
    print(f"{method:15} {bar} ({count})")

# %% [markdown]
# ### 1. What was the Most Preferred Payment Method?
# 

# %%
# Get payment method counts
preferred_payment = df['Payment Method'].value_counts()
print(f"Most Preferred Payment: {preferred_payment}")

# %%
df

# %% [markdown]
# ### 2. Which one was the Most Selling Product by Quantity and by Revenue?
# 

# %%
# Find the most selling products by quantity and revenue
print("=== MOST SELLING PRODUCTS ANALYSIS ===\n")

# 1. MOST SELLING PRODUCT BY QUANTITY
print(" MOST SELLING PRODUCT BY QUANTITY:")
print("-" * 40)

# Group by product and sum quantities
product_by_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("Top 10 Products by Quantity Sold:")
print(product_by_quantity.head(10))

# Get the top product by quantity
top_quantity_product = product_by_quantity.index[0]
top_quantity_value = product_by_quantity.iloc[0]

print(f"\n ANSWER: Most selling product by QUANTITY is '{top_quantity_product}'")
print(f"   - Total quantity sold: {top_quantity_value:,.2f}")

# 2. MOST SELLING PRODUCT BY REVENUE
print(f"\n MOST SELLING PRODUCT BY REVENUE:")
print("-" * 40)

# Calculate revenue if we have price column, otherwise ask user
if 'Price' in df.columns or 'price' in df.columns:
    price_col = 'Price' if 'Price' in df.columns else 'price'
    
    # Calculate revenue for each transaction
    df['Revenue'] = df['Quantity'] * df[price_col]
    
    # Group by product and sum revenue
    product_by_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
    print("Top 10 Products by Revenue:")
    print(product_by_revenue.head(10))
    
    # Get the top product by revenue
    top_revenue_product = product_by_revenue.index[0]
    top_revenue_value = product_by_revenue.iloc[0]
    
    print(f"\n ANSWER: Most selling product by REVENUE is '{top_revenue_product}'")
    print(f"   - Total revenue generated: ${top_revenue_value:,.2f}")
    
    # Compare quantity vs revenue leaders
    print(f"\n COMPARISON:")
    if top_quantity_product == top_revenue_product:
        print(f" Same product leads in both quantity AND revenue: {top_quantity_product}")
    else:
        print(f" Quantity leader: {top_quantity_product}")
        print(f" Revenue leader: {top_revenue_product}")
        print("   (Different products - higher-priced items may generate more revenue)")

else:
    print("  Price column not found in dataset.")
    print("   Cannot calculate revenue without price information.")
    print("   Available columns:", list(df.columns))
    print("\n   To calculate revenue, you need:")
    print("   Revenue = Quantity × Price")

# Show detailed breakdown for top products
print(f"\n DETAILED BREAKDOWN:")
print(f"\nTop 5 Products by Quantity:")
for i, (product, qty) in enumerate(product_by_quantity.head(5).items(), 1):
    print(f"  {i}. {product}: {qty:,.2f} units")

if 'Revenue' in df.columns:
    print(f"\nTop 5 Products by Revenue:")
    for i, (product, rev) in enumerate(product_by_revenue.head(5).items(), 1):
        print(f"  {i}. {product}: ${rev:,.2f}")

# %% [markdown]
# ### 3. Which City had maximum revenue, and Which Manager earned maximum revenue?
# 

# %%
# Find city with maximum revenue and manager with maximum revenue
print("=== CITY & MANAGER REVENUE ANALYSIS ===\n")

# Check if Revenue column exists (from previous calculation)
if 'Revenue' not in df.columns:
    # Calculate revenue if we have price column
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['quantity'] * df[price_col]
        print(" Revenue calculated (Quantity × Price)")
    else:
        print("  Cannot calculate revenue - Price column not found.")
        print("   Available columns:", list(df.columns))
        exit()

# 1. CITY WITH MAXIMUM REVENUE
print(" CITY WITH MAXIMUM REVENUE:")
print("-" * 40)

# Group by City and sum revenue
city_revenue = df.groupby('City')['Revenue'].sum().sort_values(ascending=False)
print("Revenue by City:")
print(city_revenue.head(10))

# Get top city
top_city = city_revenue.index[0]
top_city_revenue = city_revenue.iloc[0]

print(f"\n ANSWER: City with MAXIMUM REVENUE is '{top_city}'")
print(f"   - Total revenue: ${top_city_revenue:,.2f}")

# Show percentage of total revenue
total_revenue = df['Revenue'].sum()
city_percentage = (top_city_revenue / total_revenue) * 100
print(f"   - Represents {city_percentage:.1f}% of total company revenue")

# 2. MANAGER WITH MAXIMUM REVENUE
print(f"\n MANAGER WITH MAXIMUM REVENUE:")
print("-" * 40)

# Check if Manager column exists
manager_columns = [col for col in df.columns if 'manager' in col.lower()]
if manager_columns:
    manager_col = manager_columns[0]  # Use first manager column found
    
    # Group by manager and sum revenue
    manager_revenue = df.groupby(manager_col)['Revenue'].sum().sort_values(ascending=False)
    print(f"Revenue by {manager_col}:")
    print(manager_revenue.head(10))
    
    # Get top manager
    top_manager = manager_revenue.index[0]
    top_manager_revenue = manager_revenue.iloc[0]
    
    print(f"\n ANSWER: Manager with MAXIMUM REVENUE is '{top_manager}'")
    print(f"   - Total revenue generated: ${top_manager_revenue:,.2f}")
    
    # Show percentage of total revenue
    manager_percentage = (top_manager_revenue / total_revenue) * 100
    print(f"   - Represents {manager_percentage:.1f}% of total company revenue")
    
else:
    print("  Manager column not found in dataset.")
    print("   Looking for columns containing 'manager'...")
    print("   Available columns:", list(df.columns))

# SUMMARY COMPARISON
print(f"\n SUMMARY:")
print("=" * 50)

print(f"  Top Revenue City: {top_city} (${top_city_revenue:,.2f})")
if manager_columns:
    print(f" Top Revenue Manager: {top_manager} (${top_manager_revenue:,.2f})")
print(f" Total Company Revenue: ${total_revenue:,.2f}")

# Additional insights
print(f"\n INSIGHTS:")
city_count = len(city_revenue)
print(f"   - Total cities in dataset: {city_count}")
print(f"   - Average revenue per city: ${(total_revenue/city_count):,.2f}")
if manager_columns:
    manager_count = len(manager_revenue)
    print(f"   - Total managers in dataset: {manager_count}")
    print(f"   - Average revenue per manager: ${(total_revenue/manager_count):,.2f}")

# Show top 5 in each category
print(f"\n TOP 5 CITIES BY REVENUE:")
for i, (city, revenue) in enumerate(city_revenue.head(5).items(), 1):
    pct = (revenue/total_revenue)*100
    print(f"   {i}. {city}: ${revenue:,.2f} ({pct:.1f}%)")

if manager_columns:
    print(f"\n TOP 5 MANAGERS BY REVENUE:")
    for i, (manager, revenue) in enumerate(manager_revenue.head(5).items(), 1):
        pct = (revenue/total_revenue)*100
        print(f"   {i}. {manager}: ${revenue:,.2f} ({pct:.1f}%)")

# %% [markdown]
# ### 4. What was the Average Revenue?
# 

# %%
average_revenue = df['Revenue'].mean()
print(f"   - Average revenue per transaction: ${average_revenue:.2f}")

# %% [markdown]
# ### 5. What was the Average Revenue of November & December?
# 

# %%
# Find average revenue for November and December
print("=== AVERAGE REVENUE FOR NOVEMBER & DECEMBER ===\n")

# Check if Revenue column exists
if 'Revenue' not in df.columns:
    # Calculate revenue if we have price column
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['quantity'] * df[price_col]
        print(" Revenue calculated (Quantity × Price)")
    else:
        print(" Cannot calculate revenue - Price column not found.")
        exit()

# Convert Date column to datetime for month extraction
df['Date_datetime'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date_datetime'].dt.month
df['Month_Name'] = df['Date_datetime'].dt.month_name()

# Filter data for November (month 11) and December (month 12)
november_data = df[df['Month'] == 11]
december_data = df[df['Month'] == 12]

print(" DATE RANGE ANALYSIS:")
print(f"   - Dataset date range: {df['Date_datetime'].min().strftime('%Y-%m-%d')} to {df['Date_datetime'].max().strftime('%Y-%m-%d')}")
print(f"   - Total transactions: {len(df)}")
print(f"   - November transactions: {len(november_data)}")
print(f"   - December transactions: {len(december_data)}")

# Calculate average revenue for November
if len(november_data) > 0:
    nov_avg_revenue = november_data['Revenue'].mean()
    nov_total_revenue = november_data['Revenue'].sum()
    print(f"\n NOVEMBER RESULTS:")
    print(f"   - Average revenue per transaction: ${nov_avg_revenue:.2f}")
    print(f"   - Total revenue for November: ${nov_total_revenue:,.2f}")
    print(f"   - Number of transactions: {len(november_data)}")
else:
    print(f"\n NOVEMBER RESULTS:")
    print("   - No November data found in dataset")

# Calculate average revenue for December
if len(december_data) > 0:
    dec_avg_revenue = december_data['Revenue'].mean()
    dec_total_revenue = december_data['Revenue'].sum()
    print(f"\n  DECEMBER RESULTS:")
    print(f"   - Average revenue per transaction: ${dec_avg_revenue:.2f}")
    print(f"   - Total revenue for December: ${dec_total_revenue:,.2f}")
    print(f"   - Number of transactions: {len(december_data)}")
else:
    print(f"\n  DECEMBER RESULTS:")
    print("   - No December data found in dataset")

# Summary comparison
print(f"\n SUMMARY COMPARISON:")
print("=" * 50)

if len(november_data) > 0 and len(december_data) > 0:
    print(f" November Average Revenue: ${nov_avg_revenue:.2f}")
    print(f" December Average Revenue: ${dec_avg_revenue:.2f}")
    
    # Calculate difference
    difference = dec_avg_revenue - nov_avg_revenue
    percentage_change = (difference / nov_avg_revenue) * 100
    
    if difference > 0:
        print(f" December was ${abs(difference):.2f} higher on average ({percentage_change:+.1f}%)")
    elif difference < 0:
        print(f" November was ${abs(difference):.2f} higher on average ({percentage_change:+.1f}%)")
    else:
        print(f"  Both months had the same average revenue")
    
    # Combined average for both months
    combined_data = pd.concat([november_data, december_data])
    combined_avg = combined_data['Revenue'].mean()
    print(f"\n COMBINED NOVEMBER & DECEMBER:")
    print(f"   - Average revenue across both months: ${combined_avg:.2f}")
    print(f"   - Total transactions: {len(combined_data)}")
    print(f"   - Total revenue: ${combined_data['Revenue'].sum():,.2f}")

elif len(november_data) > 0:
    print(f" November Average Revenue: ${nov_avg_revenue:.2f}")
    print("  December: No data available")
elif len(december_data) > 0:
    print(" November: No data available")
    print(f"  December Average Revenue: ${dec_avg_revenue:.2f}")
else:
    print("  No data found for either November or December")

# Show monthly breakdown for context
print(f"\n MONTHLY REVENUE BREAKDOWN:")
monthly_avg = df.groupby('Month_Name')['Revenue'].agg(['count', 'sum', 'mean']).round(2)
monthly_avg.columns = ['Transactions', 'Total Revenue', 'Avg Revenue']
print(monthly_avg)

# %% [markdown]
# ### 5. Visual Answers

# %%
# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=== NOVEMBER & DECEMBER REVENUE VISUALIZATION ===\n")

# Check if Revenue column exists and calculate if needed
if 'Revenue' not in df.columns:
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['Quantity'] * df[price_col]
        print("✓ Revenue calculated (Quantity × Price)")
    else:
        print(" Cannot calculate revenue - Price column not found.")
        exit()

# Convert Date column to datetime and extract month information
df['Date_datetime'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date_datetime'].dt.month
df['Month_Name'] = df['Date_datetime'].dt.month_name()

# Filter data for November and December
november_data = df[df['Month'] == 11]
december_data = df[df['Month'] == 12]

# Calculate statistics
nov_exists = len(november_data) > 0
dec_exists = len(december_data) > 0

if nov_exists:
    nov_avg_revenue = november_data['Revenue'].mean()
    nov_total_revenue = november_data['Revenue'].sum()
    
if dec_exists:
    dec_avg_revenue = december_data['Revenue'].mean()
    dec_total_revenue = december_data['Revenue'].sum()

# Create comprehensive visualization
fig = plt.figure(figsize=(20, 16))

# 1. AVERAGE REVENUE COMPARISON BAR CHART
plt.subplot(2, 3, 1)

if nov_exists and dec_exists:
    months = ['November', 'December']
    avg_revenues = [nov_avg_revenue, dec_avg_revenue]
    colors = ['#FF6B35', '#F7931E']
    
    bars = plt.bar(months, avg_revenues, color=colors, alpha=0.8, 
                   edgecolor='black', linewidth=2, width=0.6)
    
    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, avg_revenues)):
        plt.text(bar.get_x() + bar.get_width()/2., value + value*0.02,
                f'${value:.2f}', ha='center', va='bottom', 
                fontweight='bold', fontsize=12)
    
    plt.title(' Average Revenue Comparison\nNovember vs December', 
              fontsize=14, fontweight='bold')
    
    # Calculate and show difference
    difference = dec_avg_revenue - nov_avg_revenue
    percentage_change = (difference / nov_avg_revenue) * 100
    
    if abs(percentage_change) > 1:  # Only show if meaningful difference
        change_text = f"{'📈' if difference > 0 else '📉'} {percentage_change:+.1f}% change"
        plt.text(0.5, max(avg_revenues) * 0.9, change_text, 
                ha='center', transform=plt.gca().transData, 
                fontsize=11, fontweight='bold', 
                color='green' if difference > 0 else 'red')

elif nov_exists:
    plt.bar(['November'], [nov_avg_revenue], color='#FF6B35', alpha=0.8)
    plt.text(0, nov_avg_revenue + nov_avg_revenue*0.02, f'${nov_avg_revenue:.2f}',
             ha='center', va='bottom', fontweight='bold', fontsize=12)
    plt.title(' Average Revenue\nNovember Only', fontsize=14, fontweight='bold')
    
elif dec_exists:
    plt.bar(['December'], [dec_avg_revenue], color='#F7931E', alpha=0.8)
    plt.text(0, dec_avg_revenue + dec_avg_revenue*0.02, f'${dec_avg_revenue:.2f}',
             ha='center', va='bottom', fontweight='bold', fontsize=12)
    plt.title(' Average Revenue\nDecember Only', fontsize=14, fontweight='bold')

plt.ylabel('Average Revenue ($)', fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 2. TOTAL REVENUE COMPARISON
plt.subplot(2, 3, 2)

if nov_exists and dec_exists:
    total_revenues = [nov_total_revenue, dec_total_revenue]
    bars = plt.bar(months, total_revenues, color=['#2E86AB', '#A23B72'], 
                   alpha=0.8, edgecolor='black', linewidth=2)
    
    # Add value labels
    for bar, value in zip(bars, total_revenues):
        plt.text(bar.get_x() + bar.get_width()/2., value + value*0.02,
                f'${value:,.0f}', ha='center', va='bottom', 
                fontweight='bold', fontsize=11, rotation=0)
    
elif nov_exists:
    plt.bar(['November'], [nov_total_revenue], color='#2E86AB', alpha=0.8)
    plt.text(0, nov_total_revenue + nov_total_revenue*0.02, f'${nov_total_revenue:,.0f}',
             ha='center', va='bottom', fontweight='bold', fontsize=11)
    
elif dec_exists:
    plt.bar(['December'], [dec_total_revenue], color='#A23B72', alpha=0.8)
    plt.text(0, dec_total_revenue + dec_total_revenue*0.02, f'${dec_total_revenue:,.0f}',
             ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.title(' Total Revenue Comparison\nNovember vs December', 
          fontsize=14, fontweight='bold')
plt.ylabel('Total Revenue ($)', fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 3. TRANSACTION COUNT COMPARISON
plt.subplot(2, 3, 3)

if nov_exists and dec_exists:
    transaction_counts = [len(november_data), len(december_data)]
    bars = plt.bar(months, transaction_counts, color=['#F18F01', '#C73E1D'], 
                   alpha=0.8, edgecolor='black', linewidth=2)
    
    # Add value labels
    for bar, value in zip(bars, transaction_counts):
        plt.text(bar.get_x() + bar.get_width()/2., value + value*0.02,
                f'{value:,}', ha='center', va='bottom', 
                fontweight='bold', fontsize=12)
                
elif nov_exists:
    plt.bar(['November'], [len(november_data)], color='#F18F01', alpha=0.8)
    plt.text(0, len(november_data) + len(november_data)*0.02, f'{len(november_data):,}',
             ha='center', va='bottom', fontweight='bold', fontsize=12)
             
elif dec_exists:
    plt.bar(['December'], [len(december_data)], color='#C73E1D', alpha=0.8)
    plt.text(0, len(december_data) + len(december_data)*0.02, f'{len(december_data):,}',
             ha='center', va='bottom', fontweight='bold', fontsize=12)

plt.title(' Number of Transactions\nNovember vs December', 
          fontsize=14, fontweight='bold')
plt.ylabel('Number of Transactions', fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# 4. REVENUE DISTRIBUTION HISTOGRAM
plt.subplot(2, 3, 4)

if nov_exists and dec_exists:
    plt.hist(november_data['Revenue'], bins=15, alpha=0.7, color='#FF6B35', 
             label=f'November (μ=${nov_avg_revenue:.2f})', edgecolor='black')
    plt.hist(december_data['Revenue'], bins=15, alpha=0.7, color='#F7931E', 
             label=f'December (μ=${dec_avg_revenue:.2f})', edgecolor='black')
    
    # Add mean lines
    plt.axvline(nov_avg_revenue, color='#FF6B35', linestyle='--', linewidth=2)
    plt.axvline(dec_avg_revenue, color='#F7931E', linestyle='--', linewidth=2)
    
elif nov_exists:
    plt.hist(november_data['Revenue'], bins=15, alpha=0.7, color='#FF6B35', 
             label=f'November (μ=${nov_avg_revenue:.2f})', edgecolor='black')
    plt.axvline(nov_avg_revenue, color='#FF6B35', linestyle='--', linewidth=2)
    
elif dec_exists:
    plt.hist(december_data['Revenue'], bins=15, alpha=0.7, color='#F7931E', 
             label=f'December (μ=${dec_avg_revenue:.2f})', edgecolor='black')
    plt.axvline(dec_avg_revenue, color='#F7931E', linestyle='--', linewidth=2)

plt.title(' Revenue Distribution\nNovember vs December', fontsize=14, fontweight='bold')
plt.xlabel('Revenue per Transaction ($)', fontweight='bold')
plt.ylabel('Frequency', fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)

# 5. MONTHLY OVERVIEW (ALL MONTHS)
plt.subplot(2, 3, 5)

monthly_avg = df.groupby('Month_Name')['Revenue'].mean().sort_values(ascending=False)
colors = ['#FF6B35' if month == 'November' else '#F7931E' if month == 'December' 
          else '#lightgray' for month in monthly_avg.index]

bars = plt.bar(range(len(monthly_avg)), monthly_avg.values, color=colors, 
               alpha=0.8, edgecolor='black', linewidth=1)

# Highlight November and December
for i, (month, value) in enumerate(monthly_avg.items()):
    if month in ['November', 'December']:
        plt.text(i, value + value*0.02, f'${value:.2f}', 
                ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.title('📅 Monthly Average Revenue Overview\n(Nov & Dec Highlighted)', 
          fontsize=14, fontweight='bold')
plt.xlabel('Month', fontweight='bold')
plt.ylabel('Average Revenue ($)', fontweight='bold')
plt.xticks(range(len(monthly_avg)), monthly_avg.index, rotation=45)
plt.grid(True, alpha=0.3, axis='y')

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 6. SUMMARY STATISTICS TABLE
plt.subplot(2, 3, 6)

# Create summary text
summary_text = "NOVEMBER & DECEMBER\nSUMMARY STATISTICS\n\n"

if nov_exists:
    summary_text += f" NOVEMBER:\n"
    summary_text += f"   Avg Revenue: ${nov_avg_revenue:.2f}\n"
    summary_text += f"   Total Revenue: ${nov_total_revenue:,.2f}\n"
    summary_text += f"   Transactions: {len(november_data):,}\n\n"

if dec_exists:
    summary_text += f" DECEMBER:\n"
    summary_text += f"   Avg Revenue: ${dec_avg_revenue:.2f}\n"
    summary_text += f"   Total Revenue: ${dec_total_revenue:,.2f}\n"
    summary_text += f"   Transactions: {len(december_data):,}\n\n"

if nov_exists and dec_exists:
    # Combined statistics
    combined_data = pd.concat([november_data, december_data])
    combined_avg = combined_data['Revenue'].mean()
    combined_total = combined_data['Revenue'].sum()
    
    summary_text += f" COMBINED (NOV + DEC):\n"
    summary_text += f" Avg Revenue: ${combined_avg:.2f}\n"
    summary_text += f" Total Revenue: ${combined_total:,.2f}\n"
    summary_text += f" Total Transactions: {len(combined_data):,}\n\n"
    
    # Comparison
    difference = dec_avg_revenue - nov_avg_revenue
    percentage_change = (difference / nov_avg_revenue) * 100
    
    if abs(percentage_change) > 0.1:
        summary_text += f" COMPARISON:\n"
        if difference > 0:
            summary_text += f"   December higher by: ${difference:.2f}\n"
        else:
            summary_text += f"   November higher by: ${abs(difference):.2f}\n"
        summary_text += f"   Percentage change: {percentage_change:+.1f}%"

plt.text(0.1, 0.9, summary_text, transform=plt.gca().transAxes, 
         fontsize=11, fontweight='normal', verticalalignment='top',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.8))

plt.axis('off')

# Adjust layout and display
plt.tight_layout()
plt.suptitle('November & December Average Revenue Analysis Dashboard', 
             fontsize=20, fontweight='bold', y=0.98)
plt.subplots_adjust(top=0.93)
plt.show()

# Create additional detailed comparison chart
if nov_exists and dec_exists:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Daily revenue trends for Nov and Dec
    nov_daily = november_data.groupby('Date_datetime')['Revenue'].sum().reset_index()
    dec_daily = december_data.groupby('Date_datetime')['Revenue'].sum().reset_index()
    
    ax1.plot(nov_daily['Date_datetime'], nov_daily['Revenue'], 
             marker='o', color='#FF6B35', linewidth=2, markersize=6, label='November')
    ax1.set_title('November Daily Revenue Trend', fontweight='bold', fontsize=14)
    ax1.set_xlabel('Date', fontweight='bold')
    ax1.set_ylabel('Daily Revenue ($)', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    ax2.plot(dec_daily['Date_datetime'], dec_daily['Revenue'], 
             marker='s', color='#F7931E', linewidth=2, markersize=6, label='December')
    ax2.set_title('December Daily Revenue Trend', fontweight='bold', fontsize=14)
    ax2.set_xlabel('Date', fontweight='bold')
    ax2.set_ylabel('Daily Revenue ($)', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # Format y-axes
    for ax in [ax1, ax2]:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    plt.tight_layout()
    plt.suptitle('Daily Revenue Trends: November vs December', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.show()

# Print summary
print(f"\n VISUALIZATION SUMMARY:")
if nov_exists and dec_exists:
    print(f"   • November Average Revenue: ${nov_avg_revenue:.2f}")
    print(f"   • December Average Revenue: ${dec_avg_revenue:.2f}")
    print(f"   • Combined Average Revenue: ${combined_avg:.2f}")
    
    difference = dec_avg_revenue - nov_avg_revenue
    percentage_change = (difference / nov_avg_revenue) * 100
    
    if difference > 0:
        print(f"   • December was ${difference:.2f} higher ({percentage_change:+.1f}%)")
    elif difference < 0:
        print(f"   • November was ${abs(difference):.2f} higher ({percentage_change:+.1f}%)")
    else:
        print(f"   • Both months had equal average revenue")
        
elif nov_exists:
    print(f"   • November Average Revenue: ${nov_avg_revenue:.2f}")
    print(f"   • December data: Not available")
elif dec_exists:
    print(f"   • November data: Not available")
    print(f"   • December Average Revenue: ${dec_avg_revenue:.2f}")
else:
    print(f"   • No data available for November or December")

print(f"\n All visualizations completed successfully!")
print(f" The charts clearly show the average revenue comparison between November and December!")

# %% [markdown]
# ### 6. What was the Standard Deviation of Revenue and Quantity?
# 

# %%
# Calculate Standard Deviation of Revenue and Quantity
print("=== STANDARD DEVIATION ANALYSIS ===\n")

# Check if Revenue column exists
if 'Revenue' not in df.columns:
    # Calculate revenue if we have price column
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['quantity'] * df[price_col]
        print(" Revenue calculated (Quantity × Price)")
    else:
        print("  Cannot calculate revenue - Price column not found.")
        print("   Will only analyze Quantity standard deviation.")

# 1. STANDARD DEVIATION OF REVENUE
if 'Revenue' in df.columns:
    revenue_std = df['Revenue'].std()
    revenue_mean = df['Revenue'].mean()
    revenue_min = df['Revenue'].min()
    revenue_max = df['Revenue'].max()
    
    print(" REVENUE STANDARD DEVIATION:")
    print("=" * 40)
    print(f"   Standard Deviation: ${revenue_std:.2f}")
    print(f"   Mean (Average): ${revenue_mean:.2f}")
    print(f"   Minimum: ${revenue_min:.2f}")
    print(f"   Maximum: ${revenue_max:.2f}")
    
    # Calculate coefficient of variation (relative variability)
    revenue_cv = (revenue_std / revenue_mean) * 100
    print(f"   Coefficient of Variation: {revenue_cv:.1f}%")
    
    # Interpretation
    print(f"\n INTERPRETATION:")
    if revenue_cv < 15:
        variability = "Low"
        interpretation = "Revenue values are quite consistent"
    elif revenue_cv < 35:
        variability = "Moderate"
        interpretation = "Revenue has moderate variability"
    else:
        variability = "High"
        interpretation = "Revenue values vary significantly"
    
    print(f"   - Variability Level: {variability}")
    print(f"   - Meaning: {interpretation}")
    print(f"   - About 68% of transactions fall within ${revenue_mean-revenue_std:.2f} to ${revenue_mean+revenue_std:.2f}")

# 2. STANDARD DEVIATION OF QUANTITY
quantity_std = df['Quantity'].std()
quantity_mean = df['Quantity'].mean()
quantity_min = df['Quantity'].min()
quantity_max = df['Quantity'].max()

print(f"\n QUANTITY STANDARD DEVIATION:")
print("=" * 40)
print(f"   Standard Deviation: {quantity_std:.2f}")
print(f"   Mean (Average): {quantity_mean:.2f}")
print(f"   Minimum: {quantity_min:.2f}")
print(f"   Maximum: {quantity_max:.2f}")

# Calculate coefficient of variation for quantity
quantity_cv = (quantity_std / quantity_mean) * 100
print(f"    Coefficient of Variation: {quantity_cv:.1f}%")

# Interpretation for quantity
print(f"\n INTERPRETATION:")
if quantity_cv < 15:
    q_variability = "Low"
    q_interpretation = "Quantity values are quite consistent"
elif quantity_cv < 35:
    q_variability = "Moderate"
    q_interpretation = "Quantity has moderate variability"
else:
    q_variability = "High"
    q_interpretation = "Quantity values vary significantly"

print(f"   - Variability Level: {q_variability}")
print(f"   - Meaning: {q_interpretation}")
print(f"   - About 68% of transactions fall within {quantity_mean-quantity_std:.2f} to {quantity_mean+quantity_std:.2f} units")

# 3. SUMMARY COMPARISON
print(f"\n SUMMARY:")
print("=" * 50)
if 'Revenue' in df.columns:
    print(f" Revenue Standard Deviation: ${revenue_std:.2f}")
    print(f"   - Coefficient of Variation: {revenue_cv:.1f}% ({variability} variability)")
print(f" Quantity Standard Deviation: {quantity_std:.2f}")
print(f"   - Coefficient of Variation: {quantity_cv:.1f}% ({q_variability} variability)")

# 4. ADDITIONAL STATISTICAL INSIGHTS
print(f"\n ADDITIONAL STATISTICS:")
print("=" * 50)

if 'Revenue' in df.columns:
    print(" REVENUE DISTRIBUTION:")
    print(f"   - Median: ${df['Revenue'].median():.2f}")
    print(f"   - 25th Percentile (Q1): ${df['Revenue'].quantile(0.25):.2f}")
    print(f"   - 75th Percentile (Q3): ${df['Revenue'].quantile(0.75):.2f}")
    print(f"   - Range: ${revenue_max - revenue_min:.2f}")
    
    # Detect potential outliers using IQR method
    q1_rev = df['Revenue'].quantile(0.25)
    q3_rev = df['Revenue'].quantile(0.75)
    iqr_rev = q3_rev - q1_rev
    lower_bound_rev = q1_rev - 1.5 * iqr_rev
    upper_bound_rev = q3_rev + 1.5 * iqr_rev
    outliers_rev = df[(df['Revenue'] < lower_bound_rev) | (df['Revenue'] > upper_bound_rev)]
    print(f"   - Potential outliers: {len(outliers_rev)} transactions")

print(f"\n QUANTITY DISTRIBUTION:")
print(f"   - Median: {df['Quantity'].median():.2f}")
print(f"   - 25th Percentile (Q1): {df['Quantity'].quantile(0.25):.2f}")
print(f"   - 75th Percentile (Q3): {df['Quantity'].quantile(0.75):.2f}")
print(f"   - Range: {quantity_max - quantity_min:.2f}")

# Detect potential outliers for quantity
q1_qty = df['Quantity'].quantile(0.25)
q3_qty = df['Quantity'].quantile(0.75)
iqr_qty = q3_qty - q1_qty
lower_bound_qty = q1_qty - 1.5 * iqr_qty
upper_bound_qty = q3_qty + 1.5 * iqr_qty
outliers_qty = df[(df['Quantity'] < lower_bound_qty) | (df['Quantity'] > upper_bound_qty)]
print(f"   - Potential outliers: {len(outliers_qty)} transactions")

print(f"\n KEY INSIGHTS:")
print("=" * 30)
print("   - Standard deviation measures spread/variability of data")
print("   - Lower std = more consistent values")
print("   - Higher std = more spread out values")
print("   - Coefficient of variation allows comparison between different scales")

# %% [markdown]
# ### 7. What was the Variance of Revenue and Quantity?
# 

# %%
# Calculate Variance of Revenue and Quantity
print("=== VARIANCE ANALYSIS ===\n")

# Check if Revenue column exists
if 'Revenue' not in df.columns:
    # Calculate revenue if we have price column
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['Quantity'] * df[price_col]  # Using 'Quantity' column
        print(" Revenue calculated (Quantity × Price)")
    else:
        print("  Cannot calculate revenue - Price column not found.")
        print("   Will only analyze Quantity variance.")

# 1. VARIANCE OF REVENUE
if 'Revenue' in df.columns:
    revenue_var = df['Revenue'].var()
    revenue_std = df['Revenue'].std()
    revenue_mean = df['Revenue'].mean()
    
    print(" REVENUE VARIANCE:")
    print("=" * 40)
    print(f"   Variance: ${revenue_var:,.2f}")
    print(f"   Standard Deviation: ${revenue_std:.2f}")
    print(f"   Mean (Average): ${revenue_mean:.2f}")
    
    # Show relationship between variance and standard deviation
    print(f"\n RELATIONSHIP:")
    print(f"   - Variance = Standard Deviation²")
    print(f"   - ${revenue_std:.2f}² = ${revenue_var:,.2f}")
    
    # Interpretation
    print(f"\n INTERPRETATION:")
    print(f"   - Variance measures the average squared deviation from the mean")
    print(f"   - Higher variance = more spread out revenue values")
    print(f"   - Revenue values typically deviate by ±${revenue_std:.2f} from the mean")

# 2. VARIANCE OF QUANTITY
quantity_var = df['Quantity'].var()
quantity_std = df['Quantity'].std()
quantity_mean = df['Quantity'].mean()

print(f"\n QUANTITY VARIANCE:")
print("=" * 40)
print(f"   Variance: {quantity_var:.2f}")
print(f"   Standard Deviation: {quantity_std:.2f}")
print(f"   Mean (Average): {quantity_mean:.2f}")

# Show relationship between variance and standard deviation
print(f"\n RELATIONSHIP:")
print(f"   - Variance = Standard Deviation²")
print(f"   - {quantity_std:.2f}² = {quantity_var:.2f}")

# Interpretation
print(f"\n INTERPRETATION:")
print(f"   - Variance measures the average squared deviation from the mean")
print(f"   - Higher variance = more spread out quantity values")
print(f"   - Quantity values typically deviate by ±{quantity_std:.2f} units from the mean")

# 3. SUMMARY COMPARISON
print(f"\n SUMMARY:")
print("=" * 50)
if 'Revenue' in df.columns:
    print(f" Revenue Variance: ${revenue_var:,.2f}")
    print(f"   - Standard Deviation: ${revenue_std:.2f}")
    print(f"   - Mean: ${revenue_mean:.2f}")

print(f" Quantity Variance: {quantity_var:.2f}")
print(f"   - Standard Deviation: {quantity_std:.2f}")
print(f"   - Mean: {quantity_mean:.2f}")

# 4. DETAILED STATISTICAL BREAKDOWN
print(f"\n DETAILED BREAKDOWN:")
print("=" * 50)

if 'Revenue' in df.columns:
    print(" REVENUE STATISTICS:")
    revenue_stats = df['Revenue'].describe()
    print(f"   - Count: {revenue_stats['count']:,.0f}")
    print(f"   - Mean: ${revenue_stats['mean']:.2f}")
    print(f"   - Std Dev: ${revenue_stats['std']:.2f}")
    print(f"   - Variance: ${df['Revenue'].var():,.2f}")
    print(f"   - Min: ${revenue_stats['min']:.2f}")
    print(f"   - 25%: ${revenue_stats['25%']:.2f}")
    print(f"   - 50% (Median): ${revenue_stats['50%']:.2f}")
    print(f"   - 75%: ${revenue_stats['75%']:.2f}")
    print(f"   - Max: ${revenue_stats['max']:.2f}")

print(f"\n QUANTITY STATISTICS:")
quantity_stats = df['Quantity'].describe()
print(f"   - Count: {quantity_stats['count']:,.0f}")
print(f"   - Mean: {quantity_stats['mean']:.2f}")
print(f"   - Std Dev: {quantity_stats['std']:.2f}")
print(f"   - Variance: {df['Quantity'].var():.2f}")
print(f"   - Min: {quantity_stats['min']:.2f}")
print(f"   - 25%: {quantity_stats['25%']:.2f}")
print(f"   - 50% (Median): {quantity_stats['50%']:.2f}")
print(f"   - 75%: {quantity_stats['75%']:.2f}")
print(f"   - Max: {quantity_stats['max']:.2f}")

# 5. VARIANCE INTERPRETATION GUIDE
print(f"\n UNDERSTANDING VARIANCE:")
print("=" * 40)
print("    What is Variance?")
print("   - Variance = Average of squared differences from the mean")
print("   - Formula: Σ(x - μ)² / N")
print("   - Units: Original units squared (e.g., dollars², units²)")
print()
print("    How to Interpret:")
print("   - Low variance = Values cluster close to mean")
print("   - High variance = Values spread widely from mean")
print("   - Variance is always positive")
print("   - Standard deviation is square root of variance")
print()
print("    Business Meaning:")
if 'Revenue' in df.columns:
    if revenue_var < (revenue_mean * 0.1) ** 2:
        rev_consistency = "Very consistent"
    elif revenue_var < (revenue_mean * 0.3) ** 2:
        rev_consistency = "Moderately consistent"
    else:
        rev_consistency = "Highly variable"
    print(f"   - Revenue: {rev_consistency} transaction values")

if quantity_var < (quantity_mean * 0.1) ** 2:
    qty_consistency = "Very consistent"
elif quantity_var < (quantity_mean * 0.3) ** 2:
    qty_consistency = "Moderately consistent"
else:
    qty_consistency = "Highly variable"
print(f"   - Quantity: {qty_consistency} order sizes")

# %% [markdown]
# ### 8. Was the revenue increasing or decreasing over the time?
# 

# %%
# Analyze Revenue Trend Over Time
print("=== REVENUE TREND ANALYSIS OVER TIME ===\n")

# Check if Revenue column exists
if 'Revenue' not in df.columns:
    # Calculate revenue if we have price column
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['Quantity'] * df[price_col]
        print(" Revenue calculated (Quantity × Price)")
    else:
        print("  Cannot calculate revenue - Price column not found.")
        exit()

# Ensure Date column is in datetime format
if 'Date_datetime' not in df.columns:
    df['Date_datetime'] = pd.to_datetime(df['Date'])

# Sort by date to analyze chronological trends
df_sorted = df.sort_values('Date_datetime')

print(" DATASET OVERVIEW:")
print(f"   - Date range: {df_sorted['Date_datetime'].min().strftime('%Y-%m-%d')} to {df_sorted['Date_datetime'].max().strftime('%Y-%m-%d')}")
print(f"   - Total time period: {(df_sorted['Date_datetime'].max() - df_sorted['Date_datetime'].min()).days} days")
print(f"   - Total transactions: {len(df_sorted)}")

# 1. DAILY REVENUE ANALYSIS
print(f"\n DAILY REVENUE TREND:")
print("=" * 40)

# Group by date and sum daily revenue
daily_revenue = df_sorted.groupby('Date_datetime')['Revenue'].sum().reset_index()
daily_revenue = daily_revenue.sort_values('Date_datetime')

# Calculate overall trend using linear correlation
import numpy as np
days_numeric = np.arange(len(daily_revenue))
correlation = np.corrcoef(days_numeric, daily_revenue['Revenue'])[0,1]

print(f"  Correlation coefficient: {correlation:.3f}")

if correlation > 0.1:
    trend_direction = "INCREASING"
    trend_strength = "Strong" if correlation > 0.5 else "Moderate" if correlation > 0.3 else "Weak"
    trend_emoji = "📈"
elif correlation < -0.1:
    trend_direction = "DECREASING"
    trend_strength = "Strong" if correlation < -0.5 else "Moderate" if correlation < -0.3 else "Weak"
    trend_emoji = "📉"
else:
    trend_direction = "STABLE"
    trend_strength = "No clear"
    trend_emoji = "➡️"

print(f"   {trend_emoji} Overall trend: {trend_direction}")
print(f"   Trend strength: {trend_strength}")

# Show first and last week averages
first_week = daily_revenue.head(7)['Revenue'].mean()
last_week = daily_revenue.tail(7)['Revenue'].mean()
change_amount = last_week - first_week
change_percentage = (change_amount / first_week) * 100 if first_week > 0 else 0

print(f"\n PERIOD COMPARISON:")
print(f"   First week average: ${first_week:,.2f}")
print(f"   Last week average: ${last_week:,.2f}")
print(f"   Change: ${change_amount:+,.2f} ({change_percentage:+.1f}%)")

# 2. MONTHLY REVENUE ANALYSIS
print(f"\n MONTHLY REVENUE TREND:")
print("=" * 40)

# Group by month
df_sorted['Year_Month'] = df_sorted['Date_datetime'].dt.to_period('M')
monthly_revenue = df_sorted.groupby('Year_Month')['Revenue'].sum().reset_index()

print("Monthly Revenue Summary:")
for i, row in monthly_revenue.iterrows():
    month_str = str(row['Year_Month'])
    revenue = row['Revenue']
    print(f"   {month_str}: ${revenue:,.2f}")

# Calculate month-to-month growth
if len(monthly_revenue) > 1:
    monthly_revenue['Revenue_Change'] = monthly_revenue['Revenue'].pct_change() * 100
    monthly_revenue['Revenue_Change_Amount'] = monthly_revenue['Revenue'].diff()
    
    print(f"\n MONTH-TO-MONTH CHANGES:")
    for i, row in monthly_revenue.iterrows():
        if i > 0:  # Skip first month (no previous month to compare)
            month_str = str(row['Year_Month'])
            change_pct = row['Revenue_Change']
            change_amt = row['Revenue_Change_Amount']
            direction = "📈" if change_pct > 0 else "📉" if change_pct < 0 else "➡️"
            print(f"   {month_str}: {direction} {change_pct:+.1f}% (${change_amt:+,.2f})")
    
    # Overall monthly trend
    avg_monthly_growth = monthly_revenue['Revenue_Change'].mean()
    print(f"\n AVERAGE MONTHLY GROWTH RATE: {avg_monthly_growth:+.1f}%")

# 3. WEEKLY REVENUE ANALYSIS
print(f"\n WEEKLY REVENUE TREND:")
print("=" * 40)

# Group by week
df_sorted['Week'] = df_sorted['Date_datetime'].dt.to_period('W')
weekly_revenue = df_sorted.groupby('Week')['Revenue'].sum().reset_index()

# Show first few and last few weeks
print("First 5 weeks:")
for i, row in weekly_revenue.head(5).iterrows():
    week_str = str(row['Week'])
    revenue = row['Revenue']
    print(f"   {week_str}: ${revenue:,.2f}")

print("...")
print("Last 5 weeks:")
for i, row in weekly_revenue.tail(5).iterrows():
    week_str = str(row['Week'])
    revenue = row['Revenue']
    print(f"   {week_str}: ${revenue:,.2f}")

# 4. SUMMARY AND CONCLUSION
print(f"\n🏁 FINAL CONCLUSION:")
print("=" * 50)

print(f" **ANSWER: Revenue was {trend_direction} over time**")
print(f"   - Trend strength: {trend_strength}")
print(f"   - Correlation: {correlation:.3f}")

if trend_direction == "INCREASING":
    print(f"    Business is growing - revenue trending upward")
elif trend_direction == "DECREASING":
    print(f"    Business declining - revenue trending downward")
else:
    print(f"    Business stable - no clear upward or downward trend")

# Additional insights
print(f"\n💡 KEY INSIGHTS:")
total_revenue = df['Revenue'].sum()
avg_daily_revenue = daily_revenue['Revenue'].mean()
best_day = daily_revenue.loc[daily_revenue['Revenue'].idxmax()]
worst_day = daily_revenue.loc[daily_revenue['Revenue'].idxmin()]

print(f"   - Total revenue: ${total_revenue:,.2f}")
print(f"   - Average daily revenue: ${avg_daily_revenue:,.2f}")
print(f"   - Best day: {best_day['Date_datetime'].strftime('%Y-%m-%d')} (${best_day['Revenue']:,.2f})")
print(f"   - Worst day: {worst_day['Date_datetime'].strftime('%Y-%m-%d')} (${worst_day['Revenue']:,.2f})")

print(f"\n TREND INTERPRETATION GUIDE:")
print("   - Correlation > 0.5: Strong upward trend")
print("   - Correlation 0.1 to 0.5: Moderate upward trend")
print("   - Correlation -0.1 to 0.1: Stable/No clear trend")
print("   - Correlation -0.5 to -0.1: Moderate downward trend")
print("   - Correlation < -0.5: Strong downward trend")

# %%
# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=== REVENUE TREND VISUALIZATION ===\n")

# Check if Revenue column exists and calculate if needed
if 'Revenue' not in df.columns:
    if 'Price' in df.columns or 'price' in df.columns:
        price_col = 'Price' if 'Price' in df.columns else 'price'
        df['Revenue'] = df['Quantity'] * df[price_col]
        print("✓ Revenue calculated (Quantity × Price)")
    else:
        print(" Cannot calculate revenue - Price column not found.")
        exit()

# Ensure Date column is in datetime format
if 'Date_datetime' not in df.columns:
    df['Date_datetime'] = pd.to_datetime(df['Date'])

# Sort by date
df_sorted = df.sort_values('Date_datetime')

# Create figure with subplots
fig = plt.figure(figsize=(20, 16))

# 1. DAILY REVENUE TREND WITH TREND LINE
plt.subplot(2, 3, 1)
daily_revenue = df_sorted.groupby('Date_datetime')['Revenue'].sum().reset_index()
daily_revenue = daily_revenue.sort_values('Date_datetime')

plt.plot(daily_revenue['Date_datetime'], daily_revenue['Revenue'], 
         marker='o', markersize=4, linewidth=1.5, alpha=0.7, color='#2E86AB')

# Add trend line
days_numeric = np.arange(len(daily_revenue))
z = np.polyfit(days_numeric, daily_revenue['Revenue'], 1)
p = np.poly1d(z)
correlation = np.corrcoef(days_numeric, daily_revenue['Revenue'])[0,1]

plt.plot(daily_revenue['Date_datetime'], p(days_numeric), 
         "--", color='red', linewidth=2, alpha=0.8, label=f'Trend (r={correlation:.3f})')

plt.title(' Daily Revenue Trend', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Revenue ($)', fontweight='bold')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# Format y-axis to show currency
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 2. CUMULATIVE REVENUE OVER TIME
plt.subplot(2, 3, 2)
daily_revenue['Cumulative_Revenue'] = daily_revenue['Revenue'].cumsum()

plt.fill_between(daily_revenue['Date_datetime'], daily_revenue['Cumulative_Revenue'], 
                 alpha=0.6, color='#A23B72')
plt.plot(daily_revenue['Date_datetime'], daily_revenue['Cumulative_Revenue'], 
         linewidth=2, color='#A23B72')

plt.title(' Cumulative Revenue Growth', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Cumulative Revenue ($)', fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 3. MONTHLY REVENUE COMPARISON
plt.subplot(2, 3, 3)
df_sorted['Year_Month'] = df_sorted['Date_datetime'].dt.to_period('M')
monthly_revenue = df_sorted.groupby('Year_Month')['Revenue'].sum().reset_index()
monthly_revenue['Month_Str'] = monthly_revenue['Year_Month'].astype(str)

bars = plt.bar(monthly_revenue['Month_Str'], monthly_revenue['Revenue'], 
               color=['#F18F01', '#C73E1D', '#2E86AB', '#A23B72', '#F18F01'][:len(monthly_revenue)],
               alpha=0.8, edgecolor='black', linewidth=0.5)

plt.title(' Monthly Revenue Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontweight='bold')
plt.ylabel('Revenue ($)', fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'${height:,.0f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 4. WEEKLY REVENUE TREND
plt.subplot(2, 3, 4)
df_sorted['Week'] = df_sorted['Date_datetime'].dt.to_period('W')
weekly_revenue = df_sorted.groupby('Week')['Revenue'].sum().reset_index()
weekly_revenue['Week_Start'] = weekly_revenue['Week'].dt.start_time

plt.plot(weekly_revenue['Week_Start'], weekly_revenue['Revenue'], 
         marker='s', markersize=6, linewidth=2, color='#C73E1D', alpha=0.8)

plt.title(' Weekly Revenue Pattern', fontsize=14, fontweight='bold')
plt.xlabel('Week Starting', fontweight='bold')
plt.ylabel('Revenue ($)', fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Format y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 5. REVENUE DISTRIBUTION (HISTOGRAM)
plt.subplot(2, 3, 5)
plt.hist(daily_revenue['Revenue'], bins=15, color='#F18F01', alpha=0.7, 
         edgecolor='black', linewidth=1)

mean_revenue = daily_revenue['Revenue'].mean()
plt.axvline(mean_revenue, color='red', linestyle='--', linewidth=2, 
           label=f'Mean: ${mean_revenue:,.0f}')

plt.title(' Daily Revenue Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Daily Revenue ($)', fontweight='bold')
plt.ylabel('Frequency', fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)

# Format x-axis
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# 6. TREND SUMMARY CHART
plt.subplot(2, 3, 6)

# Create trend summary data
trend_data = {
    'Metric': ['Correlation', 'First Week Avg', 'Last Week Avg', 'Monthly Growth'],
    'Value': [
        correlation,
        daily_revenue.head(7)['Revenue'].mean(),
        daily_revenue.tail(7)['Revenue'].mean(),
        monthly_revenue['Revenue'].pct_change().mean() if len(monthly_revenue) > 1 else 0
    ]
}

# Determine trend direction and color
if correlation > 0.1:
    trend_text = " INCREASING"
    trend_color = 'green'
elif correlation < -0.1:
    trend_text = " DECREASING"
    trend_color = 'red'
else:
    trend_text = " STABLE"
    trend_color = 'orange'

# Create text summary
plt.text(0.5, 0.8, 'REVENUE TREND SUMMARY', 
         horizontalalignment='center', fontsize=16, fontweight='bold',
         transform=plt.gca().transAxes)

plt.text(0.5, 0.6, trend_text, 
         horizontalalignment='center', fontsize=14, fontweight='bold',
         color=trend_color, transform=plt.gca().transAxes)

plt.text(0.5, 0.4, f'Correlation Coefficient: {correlation:.3f}', 
         horizontalalignment='center', fontsize=12,
         transform=plt.gca().transAxes)

# Add interpretation
if abs(correlation) > 0.5:
    strength = "Strong"
elif abs(correlation) > 0.3:
    strength = "Moderate"
elif abs(correlation) > 0.1:
    strength = "Weak"
else:
    strength = "No clear"

plt.text(0.5, 0.2, f'Trend Strength: {strength}', 
         horizontalalignment='center', fontsize=12,
         transform=plt.gca().transAxes)

plt.axis('off')

# Adjust layout and show
plt.tight_layout()
plt.suptitle('Revenue Trend Analysis Dashboard', fontsize=20, fontweight='bold', y=0.98)
plt.subplots_adjust(top=0.93)

# Show the plot
plt.show()

# Print summary statistics
print(f"\n VISUALIZATION SUMMARY:")
print(f"   • Daily revenue points plotted: {len(daily_revenue)}")
print(f"   • Date range: {daily_revenue['Date_datetime'].min().strftime('%Y-%m-%d')} to {daily_revenue['Date_datetime'].max().strftime('%Y-%m-%d')}")
print(f"   • Total revenue: ${daily_revenue['Revenue'].sum():,.2f}")
print(f"   • Average daily revenue: ${daily_revenue['Revenue'].mean():,.2f}")
print(f"   • Revenue trend: {trend_text}")


# Detailed Daily Revenue Plot with Moving Average
fig, ax = plt.subplots(figsize=(15, 8))

# Plot daily revenue
ax.plot(daily_revenue['Date_datetime'], daily_revenue['Revenue'], 
        marker='o', markersize=3, linewidth=1, alpha=0.6, color='lightblue', label='Daily Revenue')

# Add 7-day moving average
daily_revenue['MA_7'] = daily_revenue['Revenue'].rolling(window=7, center=True).mean()
ax.plot(daily_revenue['Date_datetime'], daily_revenue['MA_7'], 
        linewidth=3, color='blue', label='7-Day Moving Average')

# Add trend line
ax.plot(daily_revenue['Date_datetime'], p(days_numeric), 
        "--", color='red', linewidth=2, alpha=0.8, label=f'Linear Trend (r={correlation:.3f})')

ax.set_title('Detailed Daily Revenue Trend with Moving Average', fontsize=16, fontweight='bold')
ax.set_xlabel('Date', fontweight='bold')
ax.set_ylabel('Revenue ($)', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Format y-axis
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(" All visualizations completed successfully!")
print(f"\n INTERPRETATION GUIDE:")
print("  Upward trend: Revenue is increasing over time")
print("  Downward trend: Revenue is decreasing over time") 
print("  Stable trend: No clear increase or decrease")
print(f" Correlation > 0.5: Strong trend")
print(f" Correlation 0.1-0.5: Moderate trend")
print(f" Correlation < 0.1: Weak/No trend")

# %% [markdown]
# ### 9. What was the Average 'Quantity Sold' & 'Average Revenue' for each product
# 

# %%
# Average Quantity Sold & Average Revenue for each product
print("=== AVERAGE QUANTITY SOLD & AVERAGE REVENUE PER PRODUCT ===\n")

# Calculate revenue if not exists
if 'Revenue' not in df.columns:
    if 'Price' in df.columns:
        df['Revenue'] = df['Quantity'] * df['Price']

# Group by product and calculate averages
product_averages = df.groupby('Product').agg({
    'Quantity': ['mean', 'sum', 'count'],
    'Revenue': ['mean', 'sum']
}).round(2)

# Flatten column names
product_averages.columns = ['Avg_Quantity', 'Total_Quantity', 'Transaction_Count', 'Avg_Revenue', 'Total_Revenue']

# Sort by average revenue (descending)
product_averages = product_averages.sort_values('Avg_Revenue', ascending=False)

print("AVERAGE QUANTITY SOLD & AVERAGE REVENUE PER PRODUCT:")
print("=" * 80)
print(f"{'Product':<30} {'Avg Qty':<10} {'Avg Revenue':<15} {'Transactions':<12} {'Total Revenue':<15}")
print("-" * 80)

for product, row in product_averages.iterrows():
    print(f"{product:<30} {row['Avg_Quantity']:<10.2f} ${row['Avg_Revenue']:<14.2f} {row['Transaction_Count']:<12.0f} ${row['Total_Revenue']:<14,.2f}")

print(f"\n TOP PERFORMERS:")
print("=" * 50)

# Top 3 by average quantity
top_qty = product_averages.nlargest(3, 'Avg_Quantity')
print(" Highest Average Quantity Sold:")
for i, (product, row) in enumerate(top_qty.iterrows(), 1):
    print(f"   {i}. {product}: {row['Avg_Quantity']:.2f} units per transaction")

# Top 3 by average revenue
top_rev = product_averages.nlargest(3, 'Avg_Revenue')
print(f"\n Highest Average Revenue:")
for i, (product, row) in enumerate(top_rev.iterrows(), 1):
    print(f"   {i}. {product}: ${row['Avg_Revenue']:.2f} per transaction")

# %% [markdown]
# ### 10. What was the total number of orders or sales made?
# 

# %%
# Total number of orders or sales made
print("=== TOTAL NUMBER OF ORDERS/SALES ===\n")

# Count total number of transactions/orders
total_orders = len(df)

print(f" ANSWER: Total number of orders/sales made: {total_orders:,}")


# %% [markdown]
# ### Additional Breakdown / Further Analysis

# %%
# Additional breakdown
print(f"\n ADDITIONAL DETAILS:")
print("=" * 40)
print(f"   Total transactions: {total_orders:,}")
print(f"   Total quantity sold: {df['Quantity'].sum():,.2f}")

if 'Revenue' in df.columns or 'Price' in df.columns:
    if 'Revenue' not in df.columns:
        df['Revenue'] = df['Quantity'] * df['Price']
    print(f"   Total revenue: ${df['Revenue'].sum():,.2f}")
    print(f"   Average order value: ${df['Revenue'].mean():.2f}")

print(f"   Average quantity per order: {df['Quantity'].mean():.2f}")

# Time period
if 'Date' in df.columns:
    df['Date_temp'] = pd.to_datetime(df['Date'])
    date_range = (df['Date_temp'].max() - df['Date_temp'].min()).days
    print(f"    Time period: {date_range} days")
    if date_range > 0:
        print(f"    Average orders per day: {total_orders/date_range:.1f}")

# %%



