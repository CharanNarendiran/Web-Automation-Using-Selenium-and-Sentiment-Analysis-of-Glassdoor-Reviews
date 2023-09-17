import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()

    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, compound_score

file_path = "C:/Users/CHARAN/KGiSL/kgisl all glassdoor reviews.txt"

# Lines you want to analyze (0-indexed)
lines_to_analyze = [12, 14, 30, 32]

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for line_number in lines_to_analyze:
    if 0 <= line_number < len(lines):
        selected_line = lines[line_number].strip()
        sentiment, compound_score = perform_sentiment_analysis(selected_line)

        print(f"Line {line_number + 1}: {selected_line}")
        print(f"Sentiment: {sentiment} (Compound Score: {compound_score:.2f})\n")
    else:
        print(f"Line number {line_number + 1} is out of range.")

