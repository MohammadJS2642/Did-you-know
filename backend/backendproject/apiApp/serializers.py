from django.db import models
from rest_framework import serializers
from ModelsDB.models import DidYouKnow


class DidYouKnowSerializers(serializers.ModelSerializer):
    class Meta:
        models = DidYouKnow
        fields = (
            'text',
            'created_at',
        )
