from textblob import TextBlob
from rake_nltk import Rake
import matplotlib.pyplot as plt

# Initialize RAKE for key phrase extraction
rake_extractor = Rake()

def get_user_input():
    """Get text input from the user for analysis."""
    return input("\nEnter text to analyze: ")

def analyze_text(text):
    """Analyze text for sentiment, polarity, subjectivity, and extract key phrases."""
    if not text.strip():  # Handle empty input
        return "No text provided", 0, 0, []

    # Analyze with TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    sentiment = 'Neutral'
    
    # Determine sentiment classification
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    
    # Extract key phrases using RAKE
    rake_extractor.extract_keywords_from_text(text)
    key_phrases = rake_extractor.get_ranked_phrases()
    
    return sentiment, polarity, subjectivity, key_phrases

def display_results(sentiment, polarity, subjectivity, key_phrases):
    """Display the results of sentiment analysis."""
    print(f"\nSentiment: {sentiment}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print(f"Key Phrases: {', '.join(key_phrases) if key_phrases else 'None'}")
    print_suggestions(polarity, subjectivity)

def print_suggestions(polarity, subjectivity):
    """Provide suggestions based on sentiment analysis results."""
    print("\nSuggestions:")
    if polarity == 0:
        print("- No specific suggestions. The text is balanced.")
    elif polarity < 0:
        print("- Consider using more positive words to increase sentiment.")
    elif polarity > 0:
        print("- Try using more factual language to reduce subjectivity if needed.")

    if subjectivity > 0.5:
        print("- Try using more factual language to reduce subjectivity.")
    elif subjectivity < 0.5:
        print("- Try adding more personal or subjective expressions to increase subjectivity.")

def display_score_explanation():
    """Explain the polarity and subjectivity scores."""
    print("\nScore Explanation:")
    print("Polarity ranges from -1 (very negative) to +1 (very positive).")
    print("Subjectivity ranges from 0 (very objective) to 1 (very subjective).\n")

def visualize_sentiment(polarity, subjectivity):
    """Visualize sentiment scores using a bar chart."""
    plt.figure(figsize=(5, 3))
    plt.bar(['Polarity', 'Subjectivity'], [polarity, subjectivity], color=['skyblue', 'salmon'])
    plt.ylim(-1, 1)
    plt.title("Sentiment Analysis Visualization")
    plt.xlabel("Metrics")
    plt.ylabel("Score")
    plt.show()

def analyze_and_compare_texts(texts):
    """Analyze multiple texts and compare their sentiment scores."""
    results = []
    for text in texts:
        sentiment, polarity, subjectivity, key_phrases = analyze_text(text)
        results.append((text, sentiment, polarity, subjectivity, key_phrases))
    
    for result in results:
        text, sentiment, polarity, subjectivity, key_phrases = result
        print("\n--------------------------------------------------")
        print(f"Text: {text}")
        display_results(sentiment, polarity, subjectivity, key_phrases)
    print("\n")

# Main program execution
if __name__ == "__main__":
    display_score_explanation()
    texts = []

    while True:
        text = get_user_input()
        if text.lower() == 'exit':
            break
        texts.append(text)
        
        # Single text analysis
        sentiment, polarity, subjectivity, key_phrases = analyze_text(text)
        display_results(sentiment, polarity, subjectivity, key_phrases)
        
        # Visualization of single text sentiment
        visualize_sentiment(polarity, subjectivity)
        
    # Comparative analysis if more than one text
    if len(texts) > 1:
        analyze_and_compare_texts(texts)
