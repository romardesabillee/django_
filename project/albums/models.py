from django.db import models

class Musician(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}-({self.first_name} {self.last_name})"


class Albums(models.Model):

    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    stars = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Albums'