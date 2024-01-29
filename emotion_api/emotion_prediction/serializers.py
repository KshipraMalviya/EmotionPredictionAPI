from rest_framework import serializers
from .models import EmotionPredictionInput, EmotionPredictionOutput

class EmotionPredictionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionPredictionInput
        fields = ['sentence']

class EmotionPredictionOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionPredictionOutput
        fields = ['emotion']
