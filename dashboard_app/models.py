from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

class Data(models.Model):
	
	nom = models.CharField(max_length=100, blank=True)
	sepal_length = models.FloatField(null=True, blank=False)
	sepal_width = models.FloatField(null=True, blank=False)
	petal_length = models.FloatField(null=True, blank=False)
	petal_width = models.FloatField(null=True, blank=False)
	predictions = models.CharField(max_length=100, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		ml_model = joblib.load('ml_model_lib/ml_grene_iris_model.joblib')
		self.predictions = ml_model.predict([[self.sepal_length, self.sepal_width, self.petal_width, self.petal_length]])
		return super().save(*args, **kwargs)

class Meta:
	ordering = ['-date']

	def __str__(self):
		return self.nom
		