import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

def create_dataset_gzip_with_savings_v2(text_list):
    # Initialize two CountVectorizers to create the vocabularies
    vectorizer = CountVectorizer()
    vectorizer_gzip = CountVectorizer()

    # Compress each text in the list
    compressed_text_list = [gzip.compress(text.encode('utf-8')).decode('latin1') for text in text_list]

    # Fit the vectorizers to the text lists to create the vocabularies
    vectorizer.fit(text_list)
    vectorizer_gzip.fit(compressed_text_list)

    # Tokenize each entry in the text list using the corresponding vocabularies
    tokenized_entries = vectorizer.transform(text_list).toarray()
    tokenized_entries_gzip = vectorizer_gzip.transform(compressed_text_list).toarray()

    # Calculate the total number of tokens before and after gzip compression
    total_tokens = np.sum(tokenized_entries)
    total_tokens_gzip = np.sum(tokenized_entries_gzip)

    # Calculate the percentage of tokens saved with gzip
    percent_tokens_saved = (total_tokens - total_tokens_gzip) / total_tokens * 100

    # Create a DataFrame for the dataset
    df = pd.DataFrame()

    # Add the tokenized entries as the inputs to the dataset
    df['Input (gzip)'] = list(tokenized_entries_gzip)
    df['Input (no gzip)'] = list(tokenized_entries)

    # Add the original text as the output
    df['Output'] = text_list

    return df, percent_tokens_saved

# Create the dataset and calculate the savings
df, savings = create_dataset_gzip_with_savings_v2(selected_paragraphs)
df, savings
