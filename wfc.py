import nltk
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import string
import re

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def count_word_frequencies(text, csv_file=None):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

    # Split the text into words
    words = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Count frequencies
    word_counts = Counter(words)

    # Create a DataFrame from the counter and sort it
    df = pd.DataFrame.from_dict(word_counts, orient='index').reset_index()
    df = df.rename(columns={'index':'word', 0:'count'})
    df = df.sort_values(by='count', ascending=False)

    # Save to a CSV file, if specified
    if csv_file is not None:
        df.to_csv(csv_file, index=False)

    return df

# Test the function
text = 'Insert the text here.'
df = count_word_frequencies(text, csv_file='word_frequencies.csv')
print(df)
