from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from app_ingressos.models import Show
from app_ingressos.serializers import (
                                        ShowSerializer, ShowFinancialSerializer,
                                        )

# Create your views here.
@api_view(['GET'])
def shows(request):
    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_financial(request, show_id):
    show = Show.objects.get(id=show_id)
    serializer = ShowFinancialSerializer(show, many=False)
    return Response(serializer.data)