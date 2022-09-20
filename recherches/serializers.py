from rest_framework import serializers
from .models import TypeSquelette, Matiere, Auteur, Livre, MaisonEdition

class LivreSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = Livre
    
    
class AuteurSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = Auteur
    
class MatiereSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = Matiere
    
class TypeSqueletteSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = TypeSquelette
    

class MaisonEditionSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = MaisonEdition