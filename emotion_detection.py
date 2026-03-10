import requests
import json
def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=myObj,headers=header)
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]
    anger = emotion['emotion']['anger']
    disgust =emotion['emotion']['disgust']
    fear =emotion['emotion']['fear']
    joy = emotion['emotion']['joy']
    sadness = emotion['emotion']['sadness']
    dict_emotion = {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}
    return max(dict_emotion, key=dict_emotion.get)

