import requests,json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Get the emotion dictionary from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Create the simplified dictionary + add dominant emotion
    emotion_result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return emotion_result  # Return the response text from the API