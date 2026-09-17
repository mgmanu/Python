# Library Book Borrowing Data Analyzer 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

print("=== LIBRARY BOOK BORROWING DATA ANALYZER ===\n")

# 1. LOAD DATA
data = {
    'book_id': [1001,1002,1001,1003,1002,1001,1004,1003,1001,1002],
    'book_title': ['Python Basics','Data Science','Python Basics','Algorithms','Data Science',
                   'Python Basics','Machine Learning','Algorithms','Python Basics','Data Science'],
    'borrower_id': [101,102,103,101,104,102,105,101,103,102],
    'borrower_name': ['Alice','Bob','Charlie','Alice','David','Bob','Eve','Alice','Charlie','Bob'],
    'borrow_date': ['2025-11-01','2025-11-05','2025-11-10','2025-11-15','2025-11-20',
                   '2025-12-01','2025-12-05','2025-12-10','2025-12-15','2025-12-20'],
    'return_date': ['2025-11-15','2025-11-25','2025-11-18','2025-12-05','2025-12-05',
                   '2025-12-10','2025-12-20','2025-12-25','2025-12-25','2025-01-10'],
    'fine_paid': [0,5,0,10,0,0,0,5,0,15]
}
df = pd.DataFrame(data)

df['borrow_date'] = pd.to_datetime(df['borrow_date'])
df['return_date'] = pd.to_datetime(df['return_date'])
df['days_borrowed'] = (df['return_date'] - df['borrow_date']).dt.days
df['is_overdue'] = df['days_borrowed'] > 14
df['month_year'] = df['borrow_date'].dt.to_period('M')

print(f"Data loaded: {len(df)} records\n")

# 2. ANALYSIS
print("📚 TOP BORROWED BOOKS:")
top_books = df['book_title'].value_counts().head(5)
print(top_books)

print("\n👥 TOP BORROWERS:")
top_borrowers = df['borrower_id'].value_counts().head(5)
print(top_borrowers)

overdue_rate = (df['is_overdue'].sum() / len(df)) * 100
print(f"\n⚠️ OVERDUE RATE: {overdue_rate:.1f}%")

# 3. VISUALIZATIONS 
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Library Borrowing Analysis Dashboard', fontsize=16)

# FIXED Barplot 
sns.barplot(x=top_books.values, y=top_books.index, hue=top_books.index, 
            ax=axes[0,0], palette='viridis', legend=False)
axes[0,0].set_title('Top 5 Borrowed Books')

# Pie chart
axes[0,1].pie(top_borrowers.values, labels=top_borrowers.index.astype(str), autopct='%1.1f%%')
axes[0,1].set_title('Top Borrowers Share')

# Monthly trends
monthly = df.groupby('month_year').size()
monthly.plot(kind='line', ax=axes[1,0], marker='o', color='green', linewidth=2)
axes[1,0].set_title('Monthly Borrowing Trends')
axes[1,0].grid(True)

# Histogram
df['days_borrowed'].hist(bins=10, ax=axes[1,1], alpha=0.7, color='orange', edgecolor='black')
axes[1,1].axvline(14, color='red', linestyle='--', linewidth=2, label='14-day limit')
axes[1,1].set_title('Borrow Duration Distribution')
axes[1,1].legend()

plt.tight_layout()
plt.savefig('library_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. REPORT
print("\n📊 SUMMARY REPORT:")
report_data = {
    'Metric': ['Total Transactions', 'Unique Books', 'Unique Borrowers', 
               'Overdue Rate (%)', 'Avg Borrow Days', 'Total Fines'],
    'Value': [len(df), df['book_title'].nunique(), df['borrower_id'].nunique(),
              f"{overdue_rate:.1f}%", f"{df['days_borrowed'].mean():.1f}", df['fine_paid'].sum()]
}
report_df = pd.DataFrame(report_data)
print(report_df)
report_df.to_csv('library_summary.csv', index=False)

print("\n✅ COMPLETE!!!")

