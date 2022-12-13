from django.db import models
from django.forms import ModelForm

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    # image = models.ImageField()
    
    def __str__(self) -> str:
        return "[name : " + self.name + ", age : " + str(self.age) + ']'
    
class employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return "[name : " + self.name + ", age : " + str(self.age) + ']'
    
class product(models.Model):
    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    
    def __str__(self) -> str:
        return "[name : " + self.name + ", age : " + str(self.cost) + ']'
    
    
class image(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to="images/")
    gray = models.ImageField(upload_to="images/")
    
    def __str__(self) -> str:
        return self.title
    
class image_form(ModelForm):
    class Meta:
        model = image
        fields = ["title", "img"]