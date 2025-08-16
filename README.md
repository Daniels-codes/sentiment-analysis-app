# Sentiment Analysis Web App

A Flask web app that analyzes text sentiment (positive 😊, negative 😔, or neutral 😐) using TextBlob. Built as a project to practice Python, NLP, and web development.

## Overview
This app processes user-input text (e.g., reviews or tweets) to determine its sentiment in real-time. It features a side-by-side layout for the input form and history, an auto-clearing textarea after submission, and error handling for empty inputs. The history tracks the last 5 analyses, displayed in a compact, no-scroll UI. Developed to build skills in NLP and web development.

## Tech Stack
- Python
- Flask
- TextBlob
- HTML/CSS

## Key Features
- Real-time sentiment analysis using TextBlob.
- Side-by-side form and history layout, no page scrolling.
- Textarea clears after submission for better UX.
- Stores and displays the last 5 analyses.
- Error handling for empty inputs.
- Clean UI with a purple theme and Poppins font.

## Setup Instructions
1. Clone the repo: `git clone https://github.com/your-username/sentiment-analysis-app.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install dependencies: `pip install flask textblob`
5. Run the app: `python app.py`
6. Open `http://127.0.0.1:5000` in your browser

## Usage
- Enter text in the textarea (e.g., "I love coding").
- Click "Analyze Sentiment" to see the result (Positive 😊, Negative 😔, or Neutral 😐).
- View the last 5 analyses in the "Recent Analyses" section.

## Screenshot
![App Screenshot](screenshot.png)

## Future Improvements
- Integrate advanced NLP models (e.g., Hugging Face Transformers).
- Deploy to Render or Heroku.
- Add sentiment trend visualization.

## Author
[Daniels Praise Ifechukwu]
