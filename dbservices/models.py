from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField('Non Utilisateur', max_length = 50)
	def __str__(self):
		return self.username
	
class SuperUser(models.Model):
	supername = models.CharField('Non Validateur',max_length = 50)
	supertype = models.CharField('Type Validateur', max_length = 2)
	def __str__(self):
		return self.supername
		
class Ingredient(models.Model):
	ingname = models.CharField('Nom Ingredient',max_length = 150)
	ingtype = models.CharField('Type', max_length = 2) 
	ingnutvalue = models.IntegerField('Valeurs Nutritionnelles')
	inguser = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='suggested_ingredients', verbose_name='validateur')
	ingspuser = models.ForeignKey(SuperUser, on_delete=models.CASCADE, related_name='validated_ingredients', verbose_name='super validateur')
	def __str__(self):
		return self.ingname
	class Meta:
		ordering = ('ingtype', 'ingname', 'ingnutvalue')

class Utensil(models.Model):
	utname = models.CharField('Nom Ustensiles',max_length = 200)
	utdescr = models.CharField('Description',max_length = 500)
	utuser = models.ForeignKey(User, on_delete=models.CASCADE)
	ingspuser = models.ForeignKey(SuperUser, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.utname
	
class Action(models.Model):
	actname = models.CharField('Nom Action',max_length = 50)
	actuts = models.ForeignKey(Utensil, on_delete=models.CASCADE)
	actuser = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.actname
	
class Recipe(models.Model):
	recname = models.CharField('Nom Recettes',max_length = 100)
	recing = models.ManyToManyField(Ingredient)
	tempsprep = models.IntegerField('Temps de Préparation')
	tempscuis = models.IntegerField('Temps de Cuisson')
	description = models.CharField(max_length = 500)
	recactions = models.ManyToManyField(Action)
	recuser = models.ForeignKey(User, on_delete=models.CASCADE)
	recspuser = models.ForeignKey(SuperUser, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.recname

class Note(models.Model):
	notrec = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	notuser = models.ForeignKey(User, on_delete=models.CASCADE)
	notspuser = models.ForeignKey(SuperUser, on_delete=models.CASCADE)
	notcomm = models.CharField('Commentaires',max_length = 500)
	notnot = models.IntegerField('Nb Etoiles')
	
	def __str__(self):
		return self.notnot