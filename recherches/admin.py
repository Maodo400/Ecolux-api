from django.contrib import admin

from recherches.models import Auteur, Livre, MaisonEdition, Matiere, TypeSquelette

# Register your models here.


admin.site.register(Livre)
admin.site.register(MaisonEdition)
admin.site.register(Auteur)
admin.site.register(Matiere)
admin.site.register(TypeSquelette)

