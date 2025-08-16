from flask import Flask, request, render_template
from textblob import TextBlob
import json
import os

# Create the app
app = Flask(__name__)

# JSON file for storing history
HISTORY_FILE = "history.json"

# Load history from file (if exists)
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
else:
    history = []


# Save history to file
def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


# Define a route (main page)
@app.route("/", methods=["GET", "POST"])
# The function goes here
def home():
    sentiment = None
    text = ""
    error = None

    if request.method == 'POST':
        # Assigning the input to a variable and cutting out white spaces
        text = request.form['text'].strip()
        if not text:
            error = "Please enter some text to analyze"
        else:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity  # Get sentiment score (-1 to 1)
            if polarity > 0:
                sentiment = "Positive 😊"
            elif polarity < 0:
                sentiment = "Negative 😔"
            else:
                sentiment = "Neutral 😐"
            # Add to history (text and sentiment)
            history.append({"text": text, "sentiment": sentiment})
            # Keep only the last 5 entries
            if len(history) > 5:
                history.pop(0)

        # Save updated history to file
        save_history()
        text = "" # To clear text box after execution

    return render_template('sentiment.html', sentiment=sentiment, text=text, error=error, history=history)


if __name__ == "__main__":
    app.run(debug=True)
