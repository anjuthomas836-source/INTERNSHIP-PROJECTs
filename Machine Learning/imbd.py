# 1. Load dataset
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ABHAY\Downloads\imdb_data.csv")

# 2. Display first 10 rows
df.head(10)

# 3. Shape of dataset
df.shape

# 4. Info
df.info()

# 5. Summary statistics
df.describe()

# 6. Check & remove duplicates
df.duplicated().sum()
df = df.drop_duplicates()

# 7. Check null values
df.isnull().sum()

# 8. Handle null values
df = df.dropna()

# 9. Top 3 languages
top_languages = df['original_language'].value_counts().head(3)

# 10. Pie chart
top_languages.plot.pie(autopct='%1.1f%%')
plt.show()

# 11. Dominant languages
top_languages.index.tolist()

# 12. Extract genres
df['genres'] = df['genres'].str.replace('[','').str.replace(']','')
df['genres'] = df['genres'].str.split(',')

# 13. Count movies per genre
genre_counts = df.explode('genres')['genres'].value_counts()

# 14. Bar chart
genre_counts.plot(kind='bar')
plt.show()

# 15. Sort by popularity
df_sorted = df.sort_values(by='popularity', ascending=False)

# 16. Top 10 most popular films
top10 = df_sorted[['title', 'popularity']].head(10)

# 17. Line chart
plt.plot(top10['title'], top10['popularity'], marker='o')
plt.xticks(rotation=90)
plt.show()

# 18. Top 7 highest budget films
top_budget = df.sort_values(by='budget', ascending=False).head(7)

# 19. Titles and budgets
top_budget[['title', 'budget']]

# 20. Bar chart
plt.bar(top_budget['title'], top_budget['budget'])
plt.xticks(rotation=90)
plt.show()