import pandas as pd
import spacy
from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the dataset
df = pd.read_csv(r"C:\Users\coach\Downloads\Hyperion Dev Folder\amazon_product_reviews.csv")

# Check the column names
print(df.columns)

# Select the 'reviews.text' column and remove missing values
clean_data = df.dropna(subset=['reviews.text'])
reviews_data = clean_data['reviews.text']

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Add TextBlob integration to spaCy
nlp.add_pipe('spacytextblob')

# Define sentiment analysis function
def analyze_sentiment(review_text):
    doc = nlp(review_text)
    polarity = doc._.blob.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Example reviews
test_reviews = [
    "This product was amazing and I loved it!",
    "I didn't like this product at all. It was disappointing.",
    "It's okay, not the best but not the worst either."
]

# Analyze sentiment of each review
for review in test_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review}\nSentiment: {sentiment}\n")

