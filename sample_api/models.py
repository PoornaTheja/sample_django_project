from django.db import models

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