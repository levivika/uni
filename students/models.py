from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='clubs_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

