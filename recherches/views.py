from django.shortcuts import render
from rest_framework import generics
from .models import MaisonEdition, Auteur, Livre, Matiere, TypeSquelette
from .serializers import MaisonEditionSerializer, LivreSerializer, MatiereSerializer, TypeSqueletteSerializer, AuteurSerializer

# Create your views here.

class LivreList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Livre.objects.all()
  serializer_class = LivreSerializer
  
class LivreDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Livre.objects.all()
  serializer_class = LivreSerializer
  

class MatiereList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Matiere.objects.all()
  serializer_class = MatiereSerializer
  
class MatiereDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Matiere.objects.all()
  serializer_class = MatiereSerializer
  

class MaisonEditionList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = MaisonEdition.objects.all()
  serializer_class = MaisonEditionSerializer
  
class MaisonEditionDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = MaisonEdition.objects.all()
  serializer_class = MaisonEditionSerializer
  

class AuteurList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Auteur.objects.all()
  serializer_class = AuteurSerializer
  
class AuteurDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Auteur.objects.all()
  serializer_class = AuteurSerializer
  

class TypeSqueletteList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = TypeSquelette.objects.all()
  serializer_class = TypeSqueletteSerializer
  
class TypeSqueletteDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = TypeSquelette.objects.all()
  serializer_class = TypeSqueletteSerializer