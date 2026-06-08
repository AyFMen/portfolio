from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)        
    description = models.TextField()                
    link = models.URLField(blank=True)              
    image = models.ImageField(upload_to='projects/', blank=True)  
    date = models.DateField(auto_now_add=True)      

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)         
    level = models.IntegerField(default=50)         

    def __str__(self):
        return self.name