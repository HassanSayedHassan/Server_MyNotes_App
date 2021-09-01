from django.db import models


class Note(models.Model):
    title = models.TextField()
    disc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
