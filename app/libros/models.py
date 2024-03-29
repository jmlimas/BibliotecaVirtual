from django.db import models
from app.autores.models import Autor
 
class Libro(models.Model):
	autor = models.ManyToManyField(Autor)
	nombre = models.CharField(max_length=50)
	resumen = models.TextField(max_length=300)
	portadas = models.ImageField(upload_to='porrtadas')

	def __unicode__(self):
		return self.nombre