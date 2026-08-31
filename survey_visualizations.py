
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/DS6021-Fall26-Anonymized-cleaned.csv')


fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('DS6021 Survey Data Distributions (n=86)', fontsize=16, fontweight='bold')
axes = axes.flatten()

phone_counts = df['What type of phone do you have?'].value_counts()
axes[0].bar(phone_counts.index, phone_counts.values, color=['#0066cc', '#00a651'])
axes[0].set_title('Phone Type', fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].set_ylim(0, max(phone_counts.values) * 1.1)
for i, v in enumerate(phone_counts.values):
    axes[0].text(i, v + 1, str(v), ha='center', fontweight='bold')

sleep_hours = df['How many hours do you sleep in a typical night?'].dropna()
axes[1].hist(sleep_hours, bins=8, color='#2196f3', edgecolor='black', alpha=0.7)
axes[1].set_title('Hours of Sleep Per Night', fontweight='bold')
axes[1].set_xlabel('Hours')
axes[1].set_ylabel('Frequency')
axes[1].axvline(sleep_hours.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {sleep_hours.mean():.1f}')
axes[1].axvline(sleep_hours.median(), color='orange', linestyle='--', linewidth=2, label=f'Median: {sleep_hours.median():.1f}')
axes[1].legend()

python_prof = df['Rate your proficiency with Python'].value_counts().sort_index()
colors = ['#dc2626', '#ff6b35', '#7c3aed', '#0066cc', '#00a651']
axes[2].bar(python_prof.index, python_prof.values, color=colors[:len(python_prof)], edgecolor='black')
axes[2].set_title('Python Proficiency (1=Beginner, 5=Expert)', fontweight='bold')
axes[2].set_xlabel('Rating')
axes[2].set_ylabel('Count')
axes[2].set_xticks([1, 2, 3, 4, 5])
for i, v in enumerate(python_prof.values):
    axes[2].text(python_prof.index[i], v + 0.5, str(v), ha='center', fontweight='bold')

years_order = ['< 1 Year', '1-3 Years', '4-6 Years', '7-10 Years', '10+ Years']
years_since = df['How many years ago did you receive your undergraduate degree?'].value_counts()
years_counts = [years_since.get(y, 0) for y in years_order]
axes[3].bar(range(len(years_order)), years_counts, color=['#0066cc', '#7c3aed', '#ff6b35', '#00a651', '#dc2626'], edgecolor='black')
axes[3].set_title('Years Since Undergraduate Degree', fontweight='bold')
axes[3].set_ylabel('Count')
axes[3].set_xticks(range(len(years_order)))
axes[3].set_xticklabels(years_order, rotation=45, ha='right')
for i, v in enumerate(years_counts):
    if v > 0:
        axes[3].text(i, v + 1, str(v), ha='center', fontweight='bold')


states_visited = df['How many US states have you visited?'].dropna()
axes[4].hist(states_visited, bins=12, color='#2196f3', edgecolor='black', alpha=0.7)
axes[4].set_title('US States Visited', fontweight='bold')
axes[4].set_xlabel('Number of States')
axes[4].set_ylabel('Frequency')
axes[4].axvline(states_visited.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {states_visited.mean():.1f}')
axes[4].axvline(states_visited.median(), color='orange', linestyle='--', linewidth=2, label=f'Median: {states_visited.median():.1f}')
axes[4].legend()
axes[5].axis('off')

plt.tight_layout()
plt.show()
