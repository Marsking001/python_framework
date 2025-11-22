import pandas as pd
df = pd.read_csv('metadata.csv')
print(df.head())
print("Data loaded successfully.")

# Additional data analysis code can be added here
summary = df.describe()
print(summary)
print("Data summary generated.")
print("Data analysis completed.")
print("Data analysis script executed.")
print("Data analysis script started.")
print("Data analysis script initialized.")
print("Data analysis script running.")
print("Data analysis script finished.")
print("Data analysis script in progress.")
print("Data analysis script completed.")
print("Data analysis script executed successfully.")

# basic information about the dataset
info = df.info()
print(info)
data = {'columns': df.columns.tolist(), 'shape': df.shape}
df_info = pd.DataFrame(data)
num_rows, num_cols = df.shape
print(f"Number of rows: {num_rows}, Number of columns: {num_cols}")
df = pd.DataFrame(data)
print(df.shape)
print("Dataset information displayed.")
print("Data analysis script executed.")



# checking for missing values
missing_values = df.isnull().sum()
print(missing_values)
important_columns = df.columns.tolist()
print(f"Important columns: {important_columns}")
missing_values_important_cols = df[important_columns].isnull().sum()
numerical_stats = df.describe()
print(numerical_stats)
missing_counts = df.isnull().sum()
print("Missing values checked.")
print("Data analysis script executed.")
print(f"Missing values in each column:\n{missing_counts}")
print(f"Missing values in important columns:\n{missing_values_important_cols}")
print("missing_counts.")

# handling missing values
df_cleaned = df.dropna()
print(f"Original shape: {df.shape}, Cleaned shape: {df_cleaned.shape}")
print("Missing values handled.")
print("Data analysis script executed.")

# clean version of the dataset
df_cleaned.to_csv('data_cleaned.csv', index=False)
print("Cleaned dataset saved to 'data_cleaned.csv'.")
print("Data analysis script executed.")

# convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print("Date column converted to datetime.")
print("Data analysis script executed.")

# create new columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print("New columns 'Year', 'Month', and 'Day' created.")
print("Data analysis script executed.")

# count publications per year
publications_per_year = df['Year'].value_counts().sort_index()
print(publications_per_year)
print("Publications per year counted.")

# identify top journals publishing COVID-19 research
top_journals = df['Journal'].value_counts().head(10)
print(top_journals)
print("Top journals identified.")

# find most frequent words in titles
from collections import Counter
import re
titles = df['Title'].dropna().tolist()
words = []
for title in titles:
    words.extend(re.findall(r'\w+', title.lower()))
word_counts = Counter(words)
most_common_words = word_counts.most_common(10)
print(most_common_words)
print("Most frequent words in titles found.")

# create visualizations
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
publications_per_year.plot(kind='bar')
plt.title('Publications per Year')
plt.xlabel('Year')  
plt.ylabel('Number of Publications')
plt.savefig('publications_per_year.png')    
plt.close()
print("Visualization saved as 'publications_per_year.png'.")

#create a bar chart for top journals
plt.figure(figsize=(10, 6))
top_journals.plot(kind='bar')
plt.title('Top Journals Publishing COVID-19 Research')
plt.xlabel('Journal')
plt.ylabel('Number of Publications')
plt.savefig('top_journals.png')
plt.close()
print("Visualization saved as 'top_journals.png'.")

#generate a word cloud of paper titles
from wordcloud import WordCloud
all_titles = ' '.join(titles)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate
(all_titles)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud_titles.png')
plt.close()
print("Word cloud saved as 'wordcloud_titles.png'.")

# plot distribution of paper counts by source
source_counts = df['Source'].value_counts()
plt.figure(figsize=(10, 6))
source_counts.plot(kind='bar')
plt.title('Distribution of Paper Counts by Source')
plt.xlabel('Source')
plt.ylabel('Number of Papers')
plt.savefig('paper_counts_by_source.png')
plt.close()


# simple streamlit app to display analysis results
import streamlit as st
st.title('COVID-19 Research Data Analysis')
st.header('Publications per Year')
st.bar_chart(publications_per_year)
st.header('Top Journals Publishing COVID-19 Research')
st.bar_chart(top_journals)
st.header('Most Frequent Words in Titles')
wordcloud_image = plt.imread('wordcloud_titles.png')
st.image(wordcloud_image, caption='Word Cloud of Paper Titles')
st.header('Distribution of Paper Counts by Source')
st.bar_chart(source_counts)
print("Streamlit app code executed.")

# add interactive widgets
year_filter = st.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()), (2020, 2022))
filtered_data = df[(df['Year'] >= year_filter[0]) & (df['Year'] <= year_filter[1])]
st.write(f"Number of publications from {year_filter[0]} to {year_filter[1]}: {filtered_data.shape[0]}")
print("Interactive widgets added to Streamlit app.")    
plt.close()

# dropdown widget 
year_options = df['Year'].dropna().unique().tolist()
selected_year = st.selectbox('Select Year', year_options)
year_data = df[df['Year'] == selected_year]
st.write(f"Number of publications in {selected_year}: {year_data.shape[0]}")
print("Dropdown widget added to Streamlit app.")    
plt.close()
plt.close()

# display visualizations in streamlit
st.image('publications_per_year.png', caption='Publications per Year')
st.image('top_journals.png', caption='Top Journals Publishing COVID-19 Research')
st.image('wordcloud_titles.png', caption='Word Cloud of Paper Titles')
st.image('paper_counts_by_source.png', caption='Distribution of Paper Counts by Source')
print("Visualizations displayed in Streamlit app.")
plt.close()
plt.close()


# end of data_analysis.py
plt.close()
print("Streamlit app execution completed.")
print("Data analysis script executed.")#

