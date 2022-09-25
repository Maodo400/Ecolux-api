from rest_framework import serializers
from .models import Chapitre, TypeSquelette, Matiere, Auteur, Livre, MaisonEdition
    
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
    
class ChapitreSerializer(serializers.ModelSerializer):

  class Meta:
    model = Chapitre
    fields = ["id", "livre", "titre", "slug",]

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ["nom", "slug"]
        
        
