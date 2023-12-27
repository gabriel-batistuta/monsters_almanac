from django.db import models

# Create your models here.
class Monster(models.Model): #product_category
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to = 'monsters/', null = True, blank = True)
    # image = models.ImageField()

    #python 3
    def __str__(self):
        return self.title
    #python 2
    def __unicode__(self):
        return self.title