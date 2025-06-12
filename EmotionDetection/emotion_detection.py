# import requests
# import json

# def emotion_detector(text_to_analyse):

#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     myobj = {"raw_document": { "text": text_to_analyse } }
#     response = requests.post(url, json = myobj, headers = headers)
#     status_code = response.status_code
    
#     if status_code == 400:
#         formatted_response = { 'anger': None,
#                              'disgust': None,
#                              'fear': None,
#                              'joy': None,
#                              'sadness': None,
#                              'dominant_emotion': None }
#     else:
#         res = json.loads(response.text)
#         formatted_response = res['emotionPredictions'][0]['emotion']
#         dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
#         formatted_response['dominant_emotion'] = dominant_emotion

#     return formatted_response 
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Initialize emotion_result to None values in case of errors
    emotion_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    try:
        response = requests.post(url, json=myobj, headers=header)
        formatted_response = json.loads(response.text)
        print(formatted_response)
        if response.status_code == 200:
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            emotion_result.update({
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness'],
                'dominant_emotion': dominant_emotion
            })

        elif response.status_code == 400 or response.status_code == 500:
            # Already initialized with None values, no change needed
            pass

    except Exception as e:
        print(f"Error occurred: {e}")
        # Optionally log the exception or re-raise it
        pass

    return emotion_result
