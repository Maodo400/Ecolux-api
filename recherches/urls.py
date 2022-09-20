from django.urls import path
from .views import LivreList, LivreDetail, MatiereDetail, MatiereList, AuteurDetail, AuteurList, TypeSqueletteDetail, TypeSqueletteList, MaisonEditionDetail, MaisonEditionList

urlpatterns = [
  path("livres/<int:pk>/", LivreDetail.as_view(), name="livre_detail"),
  path("livres/", LivreList.as_view(), name="livre_list"),
  
  path("matieres/<int:pk>/", MatiereDetail.as_view(), name="matiere_detail"),
  path("matieres/", MatiereList.as_view(), name="matiere_list"),
  
  path("auteurs/<int:pk>/", AuteurDetail.as_view(), name="auteur_detail"),
  path("auteurs/", AuteurList.as_view(), name="auteur_list"),
  
  path("type_squelettes/<int:pk>/", TypeSqueletteDetail.as_view(), name="type_squelette_detail"),
  path("type_squelettes/", TypeSqueletteList.as_view(), name="type_squelette_list"),
  
  path("maison_editions/<int:pk>/", MaisonEditionDetail.as_view(), name="maison_edition_detail"),
  path("maison_editions/", MaisonEditionList.as_view(), name="maison_edition_list"),
  ]