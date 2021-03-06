from rest_framework import serializers
from .models import Wiki_model, Bmbf_model



class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wiki_model
        #fields='__all__'
        fields = '__all__'



class BmbfSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bmbf_model
        fields='__all__'