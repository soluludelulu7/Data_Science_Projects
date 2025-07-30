import pandas as pd  # Import the pandas library for data analysis

# Load the dataset from a CSV file into a DataFrame
df = pd.read_csv('bestsellers.csv')

# Show the first 5 rows of the dataset
print(df.head())

# Print the number of rows and columns in the dataset
print(df.shape)

# Print the names of all columns in the dataset
print(df.columns)

# Print basic statistics for numeric columns (mean, std, min, max, etc.)
print(df.describe())

# Remove any duplicate rows from the DataFrame
df.drop_duplicates(inplace=True)

# Rename some columns for clarity and consistency
df.rename(columns={"Name": "Title","Year": "Publication Year","User Rating": "Rating"}, inplace=True)

# Convert the 'Price' column to float type for better numerical operations
df["Price"] = df["Price"].astype(float)

# Count how many times each author appears in the dataset
author_counts = df['Author'].value_counts()
print(author_counts)

# Calculate the average rating for each genre (e.g., Fiction, Non Fiction)
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Save the top 10 most frequent authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Save the average rating per genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
