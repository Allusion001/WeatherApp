from django.db import models

class Favorites(models.Model):
  favorites = models.CharField(max_length=255)
  country = models.CharField(max_length=255,default="NS")
  favoritesdata=models.JSONField(null=True)


  def __str__(self):
        return self.favorites
 