from inspect import ArgSpec
from djongo import models
#from django.db import models
from django.forms import ModelForm


# embeded model 
class Brand(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True

    
# model form for the embeded model 
class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = (
            'name', 'tagline'
        )


class Item(models.Model):
    brand = models.EmbeddedField(
        model_container=Brand,
    )
    sku = models.IntegerField()
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title