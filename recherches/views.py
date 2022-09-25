from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from .models import Chapitre, MaisonEdition, Auteur, Livre, Matiere, TypeSquelette
from .serializers import (ChapitreSerializer, 
                          MaisonEditionSerializer, 
                          LivreSerializer, 
                          MatiereSerializer, 
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
  
# class LivreItemView(generics.ListAPIView):
#     serializer_class = ChapitreSerializer

#     def get_queryset(self):
#         return Chapitre.objects.filter(
#             livre__in=Livre.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
#         )


# class LivreListView(generics.ListAPIView):
#     queryset = Livre.objects.filter(level=1)
#     serializer_class = LivreSerializer

class ChapitreListView(generics.ListAPIView):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer


class ChapitreDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer
    
    
class LivreItemView(generics.ListAPIView):
    serializer_class = ChapitreSerializer

    def get_queryset(self):
      return Chapitre.objects.filter(
        livre__in=Livre.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )


class LivreListView(generics.ListAPIView):
    queryset = Livre.objects.filter(level=0)
    serializer_class = LivreSerializer
    