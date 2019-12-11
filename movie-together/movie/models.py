from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    rating = models.DecimalField(max_digits=4,decimal_places=2)


    def _str_(self):
        return self.title