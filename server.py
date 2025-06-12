# from flask import Flask, render_template, request
# from EmotionDetection.emotion_detection import emotion_detector

# app = Flask("Emotion Detector")

# @app.route("/emotionDetector")
# def emotion_detector_function():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = emotion_detector(text_to_analyze)
#     response_text = f"For the given statement, the system response is 'anger': \
#                     {response['anger']}, 'disgust': {response['disgust']}, \
#                     'fear': {response['fear']}, 'joy': {response['joy']}, \
#                     'sadness': {response['sadness']}. The dominant emotion is \
#                     {response['dominant_emotion']}."
#     return response_text

# @app.route("/")
# def render_index_page():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host = "0.0.0.0", port = 5000)
"""
Flask application for Emotion Detection using Watson NLP API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the provided text using the emotion_detector function.
    
    Returns:
        str: A message containing the detected emotions or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Try again."
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    return f"Emotion scores: {response}"

@app.route("/")
def render_index_page():
    """
    Render the index HTML page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5001)
