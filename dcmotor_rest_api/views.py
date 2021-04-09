from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import All_Status
from . import serializer

class AllStatusViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.AllStatusSerializer
    queryset = All_Status.objects.all()

    # def get(self, request):
    #     serializer1 = serializer.AllStatusSerializer(All_Status.objects.all(), many=True)
    #     response = {"All Status": serializer1.data}
    #     return Response(response, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     data = request.data
    #     serializer_post = serializer.AllStatusSerializer(data=data)
    #     if serializer_post.is_valid():
    #         allStatus = All_Status(**data)
    #         allStatus.save()
    #         response = serializer_post.data
    #         return Response(response, status=status.HTTP_200_OK)