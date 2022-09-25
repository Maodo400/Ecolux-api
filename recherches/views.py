from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from .models import Chapitre, Exo, MaisonEdition, Auteur, Livre, Matiere, Question, SousQuestion, TypeSquelette
from .serializers import (ChapitreSerializer, ExoSerializer, 
                          MaisonEditionSerializer, 
                          LivreSerializer, 
                          MatiereSerializer, QuestionSerializer, SousQuestionSerializer, 
                          TypeSqueletteSerializer, 
                          AuteurSerializer)

# Create your views here.

# class LivreList(generics.ListCreateAPIView):
#   # permission_classes = (IsAuthorOrReadOnly,) # new
#   queryset = Livre.objects.all()
#   serializer_class = LivreSerializer
#   filter_backends = [DjangoFilterBackend]
#   filterset_fields = ['nom']

  
# class LivreDetail(generics.RetrieveUpdateDestroyAPIView):
#   # permission_classes = (IsAuthorOrReadOnly,) # new
#   queryset = Livre.objects.all()
#   serializer_class = LivreSerializer
  

class MatiereList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Matiere.objects.all()
  serializer_class = MatiereSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['nom']
  
class MatiereDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Matiere.objects.all()
  serializer_class = MatiereSerializer
  

class MaisonEditionList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = MaisonEdition.objects.all()
  serializer_class = MaisonEditionSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['nom']
  
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
  
  

class LivreList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Livre.objects.all()
  serializer_class = LivreSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['nom']
  
class LivreDetail(generics.RetrieveUpdateDestroyAPIView):
  lookup_field = "slug"

  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Livre.objects.all()
  serializer_class = LivreSerializer
  
  
class ChapitreList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Chapitre.objects.all()
  serializer_class = ChapitreSerializer
  
class ChapitreDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  lookup_field = "slug"

  queryset = Chapitre.objects.all()
  serializer_class = ChapitreSerializer
  
  
class QuestionList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  
  
class SousQuestionList(generics.ListCreateAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = SousQuestion.objects.all()
  serializer_class = SousQuestionSerializer
  
class SousQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsAuthorOrReadOnly,) # new
  queryset = SousQuestion.objects.all()
  serializer_class = SousQuestionSerializer
    
  