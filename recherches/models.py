from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _

class MaisonEdition(models.Model):
  nom = models.CharField(max_length=50, blank=False, unique=True)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['updated_at', 'nom']
  
  def __str__(self):
    return self.nom


class Auteur(models.Model):
  nom = models.CharField(max_length=50, blank=False)
  prenom = models.CharField(max_length=50, blank=False)
  profession = models.CharField(max_length=50, blank=False)
  bio = models.TextField()
  telephone = models.CharField(max_length=20, blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['updated_at', 'nom']
  
  def __str__(self):
    return self.nom
  
  
class Matiere(models.Model):
  photo = models.ImageField(upload_to='images/', blank=True)
  nom = models.CharField(max_length=50, blank=False)
  aliases = models.CharField(max_length=50, blank=True)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['updated_at', 'nom']
  
  def __str__(self):
    return self.nom
  

class Classe(models.Model):
  rang = models.IntegerField(blank=False, unique=True)
  nom = models.CharField(max_length=50, blank=False)
  aliases = models.CharField(max_length=50, blank=True)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['updated_at', 'nom']
  
  def __str__(self):
    return self.nom
  
  
class TypeSquelette(models.Model):
  nom = models.CharField(max_length=50, blank=False)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['updated_at', 'nom']
  
  def __str__(self):
    return self.nom
  
  
class Livre(MPTTModel):
  couverture = models.ImageField(upload_to='images/', blank=True)
  nom = models.CharField(max_length=50, blank=False, unique=True)
  aliases = models.CharField(max_length=50, blank=True)
  date_publication = models.DateTimeField(auto_now=True)
  description = models.TextField(null=True)
  est_corrige = models.BooleanField(default=False)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  # auteurs = models.ManyToManyField(Auteur, null=True)  
  # maison_edition = models.ForeignKey(MaisonEdition, on_delete=models.CASCADE, null=True)
  # matieres = models.ManyToManyField(Matiere, null=True)  
  # type_squelette = models.ForeignKey(TypeSquelette, on_delete=models.CASCADE, null=True)
  # classes = models.ManyToManyField(Classe, null=True)

  slug = models.SlugField(
        verbose_name=_("Livre safe URL"), max_length=255, unique=True)
  parent = TreeForeignKey(
    "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

  class MPTTMeta:
        order_insertion_by = ["nom"]

  class Meta:
        verbose_name = _("Livre")
        verbose_name_plural = _("Livres")
      
      
class Chapitre(models.Model):
    """
    The Chapitre table contining all Chapitre items.
    """
    
    titre = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    livre = models.ForeignKey(Livre, on_delete=models.RESTRICT)

    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ("created_at",)
        verbose_name = _("Chapitre")
        verbose_name_plural = _("Chapitres")

    def __str__(self):
        return self.titre
      

  
  
# class Exo(models.Model):
#   titre = models.CharField(max_length=150, blank=False)
#   description = models.TextField()
#   updated_at = models.DateTimeField(auto_now=True)
#   created_at = models.DateTimeField(auto_now_add=True)
#   chapitre = models.ForeignKey(Chapitre, on_delete=models.RESTRICT)

#   slug = models.SlugField(max_length=255)

#   class Meta:
#         ordering = ("created_at",)
#         verbose_name = _("Exo")
#         verbose_name_plural = _("Exos")

#   def __str__(self):
#         return self.titre