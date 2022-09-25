from rest_framework import serializers
from .models import Chapitre, Exo, Question, SousQuestion, TypeSquelette, Matiere, Auteur, Livre, MaisonEdition
    
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

class ExoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Exo
    fields = '__all__'
      
class ChapitreSerializer(serializers.ModelSerializer):
  exos = ExoSerializer(read_only=True, many=True)

  class Meta:
    model = Chapitre
    fields = '__all__'
        

        
class QuestionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Question
    fields = '__all__'

class SousQuestionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = SousQuestion
    fields = '__all__'
    
class LivreSerializer(serializers.ModelSerializer):
    chapitres = ChapitreSerializer(read_only=True, many=True)
    class Meta:
      model = Livre
      fields = '__all__'