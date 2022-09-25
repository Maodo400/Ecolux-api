from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from recherches.models import Auteur, Chapitre, Classe, Livre, MaisonEdition, Matiere, TypeSquelette

admin.site.register(Livre, MPTTModelAdmin)
admin.site.register(Chapitre)
