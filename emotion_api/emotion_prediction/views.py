import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from .mainlogic import predict_emotion
from django.views.decorators.csrf import csrf_exempt

base_dir = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(base_dir, 'mainlogic.py')

@csrf_exempt
def predict_emotion_view(request):
    if request.method == 'POST':
        input_text = json.loads(request.body).get('input_text', '')
        print("Input text: ",input_text)
        if input_text:
            predicted_emotion, label = predict_emotion(input_text)
            response_data = {
                'predicted_emotion': predicted_emotion,
                'label': int(label),
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Please enter some text!'}, status=400)
