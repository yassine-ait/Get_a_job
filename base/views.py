

from django.db.models.base import Model
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views import View
from .offres import offres
from .models import Offre
from .models import Recruter
from .models import Postule
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OffreSerializer
from .serializers import RecruterSerializer
from .serializers import PostuleSerializer
from rest_framework import status


# Create your views here.


class MyRoutes(APIView):
    def get(self, request):
        return Response('Hello world')


class OffresList(APIView):
    def get(self, request):
        offres = Offre.objects.all()
        serializer = OffreSerializer(offres, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {

            'image': request.data.get('image'),
            'name': request.data.get('name'),
            'namecampany': request.data.get('namecampany'),
            'description': request.data.get('description'),
            'category': request.data.get('category'),
            'tipetime': request.data.get('tipetime'),
            'experience': request.data.get('experience'),
            'diplome': request.data.get('diplome'),
            'salaire': request.data.get('salaire'),
            'contrat': request.data.get('contrat'),
            'region': request.data.get('region'),
            'date': request.data.get('date'),
        }

        serializer = OffreSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OffreView(APIView):
    def get(self, request, pk):
        offre = Offre.objects.get(id=pk)
        serializer = OffreSerializer(offre, many=False)

        return Response(serializer.data)

    def delete(self, request, pk):
        offre = Offre.objects.get(id=pk)
        print("delete")
        offre.delete()
        return Response({'Offre deleted'}, status=status.HTTP_200_CREATED)


# Recruter...............................................................................................


class RecrutersList(APIView):
    def get(self, request):
        recruters = Recruter.objects.all()
        serializer = RecruterSerializer(recruters, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'nom': request.data.get('nom'),
            'prenom': request.data.get('prenom'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'civilite': request.data.get('civilite'),
            'telephone': request.data.get('telephone'),
            'namecampany': request.data.get('namecampany'),

        }

        serializer = RecruterSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruterLogin(APIView):
    def get(self, request, pk):
        recruter = Recruter.objects.get(id=pk)
        serializer = RecruterSerializer(recruter, many=False)
        return(serializer.data)


# Postule...............................................................................................
class PostulesList(APIView):

    def get(self, request, pk, namec):
        postules = Postule.objects.all(id=pk, namecampany=namec)
        serializer = PostuleSerializer(postules, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'nom': request.data.get('nom'),
            'prenom': request.data.get('prenom'),
            'email': request.data.get('email'),
            'motivation': request.data.get('motivation'),
            'cvfile': request.data.get('cvfile'),
            'idoffre': request.data.get('idoffre'),
            'namecampany': request.data.get('namecampany'),

        }

        serializer = PostuleSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostuleDisplay(APIView):
    def get(self, request):
        postulesdisplay = Postule.objects.all()
        serializer = PostuleSerializer(postulesdisplay, many=True)
        return Response(serializer.data)
