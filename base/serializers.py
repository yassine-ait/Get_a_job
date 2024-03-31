from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Offre
from .models import Recruter
from .models import Postule


class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'


class RecruterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruter
        fields = '__all__'


class PostuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postule
        fields = '__all__'
