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
  
class SousQuestion(models.Model):
  numero = models.IntegerField(auto_created=True)
  titre = models.CharField(max_length=150, blank=False)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(unique=True)

  class Meta:
        ordering = ("numero",)
        verbose_name = _("Sous Question")
        verbose_name_plural = _("Sous Questions")

  def __str__(self):
        return self.titre 
  
  
class Question(models.Model):
  numero = models.IntegerField(auto_created=True)
  titre = models.CharField(max_length=150, blank=False)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  sous_questions = models.ManyToManyField(SousQuestion, blank=True)  
  slug = models.SlugField(unique=True)


  class Meta:
        ordering = ("numero",)
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

  def __str__(self):
        return self.titre    

class Exo(models.Model):
  numero = models.IntegerField(auto_created=True) 
  titre = models.CharField(max_length=150, blank=False)
  description = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  questions = models.ManyToManyField(Question, blank=True)  
  slug = models.SlugField(unique=True)

  class Meta:
        ordering = ("numero",)
        verbose_name = _("Exo")
        verbose_name_plural = _("Exos")

  def __str__(self):
        return self.titre
  
class Chapitre(models.Model):

    titre = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    exos = models.ManyToManyField(Exo, blank=True)  
    slug = models.SlugField(unique=True)

    class Meta:
      ordering = ("titre",)
      verbose_name = _("Chapitre")
      verbose_name_plural = _("Chapitres")
       

      
class Livre(models.Model):
  couverture = models.ImageField(upload_to='images/', blank=True)
  nom = models.CharField(max_length=50, blank=False, unique=True)
  aliases = models.CharField(max_length=50, blank=True)
  date_publication = models.DateTimeField(auto_now=True)
  description = models.TextField(null=True)
  est_corrige = models.BooleanField(default=False)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  chapitres = models.ManyToManyField(Chapitre, blank=True)  
  slug = models.SlugField(unique=True)


  auteurs = models.ManyToManyField(Auteur, blank=True, null=True)  
  maison_edition = models.ForeignKey(MaisonEdition, on_delete=models.CASCADE, blank=True, null=True)
  matieres = models.ManyToManyField(Matiere, blank=True, null=True)  
  type_squelette = models.ForeignKey(TypeSquelette, on_delete=models.CASCADE, blank=True, null=True)
  classes = models.ManyToManyField(Classe, blank=True, null=True)

  class Meta:
        verbose_name = _("Livre")
        verbose_name_plural = _("Livres")
      
  