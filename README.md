# Sentiment Analysis Tool 📊

## Project Overview
The **Sentiment Analysis Tool** is designed to evaluate user-provided text by classifying sentiment (positive, negative, neutral), measuring polarity and subjectivity, extracting key phrases, and providing suggestions for sentiment modification. With a bar chart for visualization and comparative analysis across multiple texts, this tool offers a comprehensive approach to understanding and leveraging sentiment insights.

### Purpose
This tool is ideal for various applications, including:
- **Customer Feedback Analysis**: Understand customer sentiment in reviews to improve products and services.
- **Social Media Monitoring**: Track trends and public opinion on platforms like Twitter or Facebook.
- **Product or Service Insights**: Identify themes in customer feedback, highlighting positive or negative patterns.

### Goals
- **Classify Sentiment**: Identify if text is positive, negative, or neutral.
- **Measure Polarity and Subjectivity**: Provide polarity (degree of positivity/negativity) and subjectivity (extent of opinion).
- **Extract Key Phrases**: Identify important phrases that contribute to sentiment.
- **Provide Suggestions**: Offer tips for modifying sentiment if desired.
- **Enable Comparative Analysis**: Analyze and compare sentiment across multiple texts.

## Code Structure
The code is organized into modular functions for easy maintenance and readability.

### Key Functions
- **`get_user_input()`**: Prompts the user to enter text.
- **`analyze_text(text)`**: Analyzes text for sentiment, polarity, subjectivity using TextBlob, and extracts key phrases using RAKE.
- **`display_results(sentiment, polarity, subjectivity, key_phrases)`**: Outputs sentiment analysis results to the user.
- **`print_suggestions(polarity, subjectivity)`**: Provides tips based on the text's polarity and subjectivity scores.
- **`display_score_explanation()`**: Explains what polarity and subjectivity scores mean.
- **`visualize_sentiment(polarity, subjectivity)`**: Generates a bar chart of polarity and subjectivity scores.
- **`analyze_and_compare_texts(texts)`**: Allows multiple texts to be analyzed and compared for broader insights.

Usage Instructions

Follow these steps to use the Sentiment Analysis Tool:

    Run the Code: Ensure Python and the required libraries are installed, then execute the script.
    Input Text: Enter the text you'd like to analyze when prompted. Type exit to finish.
    Results Interpretation:
        Sentiment: Displays positive, negative, or neutral sentiment based on polarity.
        Polarity Score: Measures positivity/negativity on a scale from -1 (negative) to +1 (positive).
        Subjectivity Score: Ranges from 0 (objective) to 1 (subjective), indicating the level of opinion.
        Key Phrases: Highlights important phrases impacting sentiment.
    Suggestions: Provides tips for adjusting sentiment or subjectivity if needed.
    Visualization: View a bar chart of polarity and subjectivity scores for a visual understanding of the text's sentiment.

Example Usage

Enter text to analyze: "The service was amazing and the product exceeded expectations."

Output:
    Sentiment: Positive
    Polarity: 0.75
    Subjectivity: 0.9
    Key Phrases: service, amazing, exceeded expectations
Libraries Used

The tool leverages several Python libraries:

    TextBlob: Performs sentiment analysis.
    RAKE: Extracts key phrases impacting sentiment.
    Matplotlib: Creates a bar chart visualization for polarity and subjectivity scores.

Explanation of Metrics

    Polarity: Ranges from -1 (negative) to +1 (positive); higher scores indicate more positive sentiment.
    Subjectivity: Ranges from 0 (objective) to 1 (subjective), measuring how factual or opinionated the text is.

Limitations and Error Handling

    Sarcasm Detection: The tool may misinterpret sarcasm, leading to incorrect sentiment classification.
    Domain-Specific Language: Industry-specific terminology may result in misclassifications.
    Empty Input: The tool includes error handling for empty inputs.

Troubleshooting Tips

    Missing Libraries: Install any missing packages with pip install <package-name>.
    RAKE Extraction Issues: Ensure RAKE keyword lists are loaded correctly.
    Matplotlib Errors: Confirm that matplotlib is installed and configured for your environment.

Future Improvements

Looking ahead, the tool could benefit from:

    Improved Sarcasm Detection: Integrate advanced NLP models to better understand sarcastic language.
    Enhanced Comparative Visualization: Add advanced charts to better highlight differences across multiple texts.
    Web Interface: Develop a web-based interface using Flask or Streamlit for a more interactive experience.

Happy Analyzing! 😊
