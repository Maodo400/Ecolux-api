from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from recherches.models import Auteur, Chapitre, Classe, Exo, Livre, MaisonEdition, Matiere, Question, SousQuestion, TypeSquelette

admin.site.register(Livre)
admin.site.register(Chapitre)
admin.site.register(Exo)
admin.site.register(Question)
admin.site.register(SousQuestion)