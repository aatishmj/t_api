from rest_framework import serializers
from .models import User, DashboardData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']

class DashboardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardData
        fields = ['income', 'income_goal', 'risk']
