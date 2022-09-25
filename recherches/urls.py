from django.urls import path, re_path
from .views import ChapitreDetail, ChapitreList, LivreDetail, LivreList, MatiereDetail, MatiereList, AuteurDetail, AuteurList, TypeSqueletteDetail, TypeSqueletteList, MaisonEditionDetail, MaisonEditionList

app_name = "store"

urlpatterns = [
  
  path("livres/<slug:slug>/", LivreDetail.as_view(), name="livre_detail"),
  path("livres/", LivreList.as_view(), name="livre_list"),
  
  path("chapitres/<slug:slug>/", ChapitreDetail.as_view(), name="chapitre_detail"),
  path("chapitres/", ChapitreList.as_view(), name="chapitre_list"),
  
  path("matieres/<int:pk>/", MatiereDetail.as_view(), name="matiere_detail"),
  path("matieres/", MatiereList.as_view(), name="matiere_list"),
  
  path("auteurs/<int:pk>/", AuteurDetail.as_view(), name="auteur_detail"),
  path("auteurs/", AuteurList.as_view(), name="auteur_list"),
  
  path("type_squelettes/<int:pk>/", TypeSqueletteDetail.as_view(), name="type_squelette_detail"),
  path("type_squelettes/", TypeSqueletteList.as_view(), name="type_squelette_list"),
  
  path("maison_editions/<int:pk>/", MaisonEditionDetail.as_view(), name="maison_edition_detail"),
  path("maison_editions/", MaisonEditionList.as_view(), name="maison_edition_list"),
  
  # path("livres/", LivreListView.as_view(), name="livres"),
  # path("livres/<slug:slug>/", LivreItemView.as_view(), name="livre_item"),
  # path("livres/<slug:slug>/<slug:slugChap>/", ChapitreListView.as_view(), name="livre_item"),
  #     # path("chapitres/", ChapitreListView.as_view(), name="store_home"),
  #     # path("chapitres/<slug:slug>/", ChapitreDetail.as_view(), name="chapitre"),
]