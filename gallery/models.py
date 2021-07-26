from django.db import models


class Collection(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Image(models.Model):
    name = models.CharField(max_length=254)
    collection = models.ForeignKey(
        'Collection', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()
    upvote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
