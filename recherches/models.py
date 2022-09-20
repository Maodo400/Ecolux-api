from django.db import models

class MaisonEdition(models.Model):
  nom = models.CharField(max_length=50, blank=False, unique=True)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['nom']
  
  def __str__(self):
    return self.nom


class Auteur(models.Model):
  nom = models.CharField(max_length=50, blank=False)
  prenom = models.CharField(max_length=50, blank=False)
  profession = models.CharField(max_length=50, blank=False)
  bio = models.TextField()
  telephone = models.CharField(max_length=20, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['nom']
  
  def __str__(self):
    return self.nom
  
  
class Matiere(models.Model):
  photo = models.ImageField(upload_to='images/', blank=True)
  nom = models.CharField(max_length=50, blank=False)
  aliases = models.CharField(max_length=50, blank=True)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['nom']
  
  def __str__(self):
    return self.nom
  
class TypeSquelette(models.Model):
  nom = models.CharField(max_length=50, blank=False)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['nom']
  
  def __str__(self):
    return self.nom
  
  
class Livre(models.Model):
  couverture = models.ImageField(upload_to='images/', blank=True)
  nom = models.CharField(max_length=50, blank=False)
  aliases = models.CharField(max_length=50, blank=True)
  date_publication = models.DateTimeField()
  description = models.TextField()
  est_corrige = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  auteurs = models.ManyToManyField(Auteur)  
  maison_edition = models.ForeignKey(MaisonEdition, on_delete=models.CASCADE)
  matieres = models.ManyToManyField(Matiere)  
  type_squelette = models.ForeignKey(TypeSquelette, on_delete=models.CASCADE)



  class Meta:
    ordering = ['nom']
  
  def __str__(self):
    return self.nom
  

  
  