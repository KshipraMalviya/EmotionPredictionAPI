from django.db import models

class EmotionPredictionInput(models.Model):
    sentence = models.TextField()

class EmotionPredictionOutput(models.Model):
    emotion = models.CharField(max_length=255)
    label =models.IntegerField()
