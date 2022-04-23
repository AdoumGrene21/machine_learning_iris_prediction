from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
	list_display = ('nom', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'predictions')

admin.site.register(Data, DataAdmin)
