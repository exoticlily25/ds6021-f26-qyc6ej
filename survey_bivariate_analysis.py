"""
Bivariate analysis of survey data - relationships between pairs of variables.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/DS6021-Fall26-Anonymized-cleaned.csv')

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('DS6021 Survey: Bivariate Relationships', fontsize=16, fontweight='bold')
axes = axes.flatten()

python_sql = pd.crosstab(df['Rate your proficiency with Python'], df['Have you ever used SQL?'])
python_sql.plot(kind='bar', ax=axes[0], color=['#ff6b35', '#0066cc'], edgecolor='black')
axes[0].set_title('Python Proficiency vs SQL Experience', fontweight='bold')
axes[0].set_xlabel('Python Proficiency Rating')
axes[0].set_ylabel('Count')
axes[0].legend(title='SQL Used?', labels=['No', 'Yes'])
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)

sleep_by_python = [df[df['Rate your proficiency with Python'] == i]['How many hours do you sleep in a typical night?'].dropna().values
                   for i in sorted(df['Rate your proficiency with Python'].dropna().unique())]
axes[1].boxplot(sleep_by_python, labels=sorted(df['Rate your proficiency with Python'].dropna().unique()))
axes[1].set_title('Python Proficiency vs Sleep Hours', fontweight='bold')
axes[1].set_xlabel('Python Proficiency Rating')
axes[1].set_ylabel('Hours of Sleep')
axes[1].grid(axis='y', alpha=0.3)

years_order = {'< 1 Year': 0.5, '1-3 Years': 2, '4-6 Years': 5, '7-10 Years': 8.5, '10+ Years': 12}
df['years_numeric'] = df['How many years ago did you receive your undergraduate degree?'].map(years_order)
scatter_data = df[df['years_numeric'].notna() & df['How many US states have you visited?'].notna()]
axes[2].scatter(scatter_data['years_numeric'], scatter_data['How many US states have you visited?'],
                alpha=0.6, s=80, color='#2196f3', edgecolor='black', linewidth=0.5)
axes[2].set_title('Years Since Degree vs States Visited', fontweight='bold')
axes[2].set_xlabel('Years Since Undergraduate Degree')
axes[2].set_ylabel('Number of US States Visited')
axes[2].grid(alpha=0.3)
z = np.polyfit(scatter_data['years_numeric'], scatter_data['How many US states have you visited?'], 1)
p = np.poly1d(z)
axes[2].plot(scatter_data['years_numeric'].sort_values(),
             p(scatter_data['years_numeric'].sort_values()),
             "r--", linewidth=2, label='Trend line')
axes[2].legend()

phone_python = pd.crosstab(df['What type of phone do you have?'], df['Rate your proficiency with Python'])
phone_python.plot(kind='bar', ax=axes[3], color=['#dc2626', '#ff6b35', '#7c3aed', '#0066cc', '#00a651'],
                  edgecolor='black')
axes[3].set_title('Phone Type vs Python Proficiency', fontweight='bold')
axes[3].set_xlabel('Phone Type')
axes[3].set_ylabel('Count')
axes[3].legend(title='Python Rating', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
axes[3].set_xticklabels(axes[3].get_xticklabels(), rotation=0)

git_python = pd.crosstab(df['Rate your proficiency with git/github'], df['Rate your proficiency with Python'])
im = axes[4].imshow(git_python.values, cmap='YlOrRd', aspect='auto')
axes[4].set_xticks(range(len(git_python.columns)))
axes[4].set_yticks(range(len(git_python.index)))
axes[4].set_xticklabels(git_python.columns)
axes[4].set_yticklabels(git_python.index)
axes[4].set_title('Git/GitHub vs Python Proficiency (Heatmap)', fontweight='bold')
axes[4].set_xlabel('Python Proficiency')
axes[4].set_ylabel('Git/GitHub Proficiency')
for i in range(len(git_python.index)):
    for j in range(len(git_python.columns)):
        text = axes[4].text(j, i, git_python.values[i, j],
                           ha="center", va="center", color="black", fontweight='bold')
plt.colorbar(im, ax=axes[4], label='Count')

years_order_list = ['< 1 Year', '1-3 Years', '4-6 Years', '7-10 Years', '10+ Years']
sql_years = pd.crosstab(df['How many years ago did you receive your undergraduate degree?'],
                         df['Have you ever used SQL?'])
sql_years = sql_years.reindex(years_order_list)
sql_years.plot(kind='bar', ax=axes[5], color=['#ff6b35', '#0066cc'], edgecolor='black')
axes[5].set_title('SQL Experience vs Years Since Degree', fontweight='bold')
axes[5].set_xlabel('Years Since Degree')
axes[5].set_ylabel('Count')
axes[5].legend(title='SQL Used?', labels=['No', 'Yes'])
axes[5].set_xticklabels(axes[5].get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()
