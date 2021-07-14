from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import DidYouKnowSerializers
from ModelsDB.models import DidYouKnow

# Create your views here.


class ShowData(APIView):
    def get(self, request, *args, **kwargs):
        querySets = DidYouKnow.objects.al()
        serializers = DidYouKnowSerializers(querySets, many=True)

        return Response(serializers.data)
