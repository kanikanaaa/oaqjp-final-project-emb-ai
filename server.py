""" Main module to run the application Emotion detector """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app:
app = Flask("Emotion detector")

""" The main module for application emotionDetector """
@app.route("/emotionDetector") # as referenced in the mywebscript.js file
def emo_detector():
    """ main function """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Error handling
    if dominant_emotion is None: # when blank is provided
        return "Invalid text! Please try again!"
    # When not blank, return a formatted string
    return f"For the given statement, the system response is 'anger': {anger}, \
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.\
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page(): # present the web interface
    """ function to present the web interface """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
