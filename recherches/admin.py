from django.contrib import admin
from recherches.models import Auteur, Chapitre, Classe, Exo, Livre, MaisonEdition, Matiere, Question, SousQuestion, TypeSquelette

admin.site.register(Livre)
admin.site.register(Chapitre)
admin.site.register(Exo)
admin.site.register(Question)
admin.site.register(SousQuestion)
admin.site.register(Auteur)
admin.site.register(Classe)
admin.site.register(MaisonEdition)
admin.site.register(Matiere)
admin.site.register(TypeSquelette)
