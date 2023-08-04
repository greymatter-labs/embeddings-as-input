
# Text Compression and Tokenization Experiment

This repository contains an experiment where texts are compressed using gzip, tokenized, and compared to the tokenization of the original texts.

Achieves a 15% token compression ratio. 

This dataset will be used to generate a model that converts back to english. From there, we will start actually transforming the directly embedded input.

## Description of the Experiment

A list of strings (in this case, paragraphs from the book "1984") are tokenized both before and after gzip compression. The resulting token counts are compared to calculate the percentage of tokens saved by using gzip compression.

Two separate `CountVectorizer` instances are used to tokenize the original and compressed texts, as they have different vocabularies.

The main function, `create_dataset_gzip_with_savings_v2`, performs the following steps:

1. Compresses each text in the list using gzip.
2. Fits a `CountVectorizer` to both the original and compressed text lists to create separate vocabularies.
3. Tokenizes each entry in the text list using the corresponding vocabularies.
4. Calculates the total number of tokens before and after gzip compression.
5. Calculates the percentage of tokens saved with gzip.
6. Returns a pandas DataFrame containing the tokenized entries (both with and without gzip compression) as the inputs, and the original text as the output. Also returns the overall percentage of tokens saved with gzip.

The experiment found that on average, gzip compression reduced the number of tokens by about 15.26% across 1000 random paragraphs from "1984".

## Usage

The function `create_dataset_gzip_with_savings_v2` can be used with any list of strings. The function returns a pandas DataFrame and the overall percentage of tokens saved with gzip.

```python
df, savings = create_dataset_gzip_with_savings_v2(selected_paragraphs)
```

## Limitations and Considerations

The percentage of tokens saved with gzip compression can vary depending on the specifics of the text. The 15.26% figure is an average across all paragraphs used in this experiment.

This experiment uses simple tokenization based on word counts and does not consider more complex linguistic features. The token counts are meant to provide a simple measure of the information content of the texts and are not intended to capture all aspects of the texts' meanings or structures.
