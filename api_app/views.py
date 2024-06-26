from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, DashboardData
from .serializers import UserSerializer, DashboardDataSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_dashboard_data(request):
    user = User.objects.get(id=request.data['user_id'])
    serializer = DashboardDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
