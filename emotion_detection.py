import requests # Import the requests library to handle HTTP requests
import json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):

    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion scores from the response
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    # compare each score and determine dominant_emotion - testing
    max_value = max(float(anger), float(disgust), float(fear), float(joy), float(sadness))
    if float(anger) == max_value:
        dominant_emotion = "anger"
    elif float(disgust) == max_value:
        dominant_emotion = "disgust"
    elif float(fear) == max_value:
        dominant_emotion = "fear"
    elif float(joy) == max_value:
        dominant_emotion = "joy"
    else: 
        dominant_emotion = "sadness"

    # Returning score for each emotion
    return {"anger": anger, 
    "disgust": disgust, 
    "fear": fear, 
    "joy": joy, 
    "sadness": sadness,
    "dominant_emotion": dominant_emotion}
    # return response.text