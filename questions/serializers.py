from rest_framework import serializers
from .models import Paper_model

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paper_model
        fields='__all__'


