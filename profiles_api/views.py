from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview =[
            'Uses HTTP method as functions (get, post, patch(partially update), put, delete)'
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            'first APIViews features list',
        ]

        return Response({'message':'Hello!', 'APIViews':an_apiview})