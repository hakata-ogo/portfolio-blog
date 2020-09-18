from django.db import models

# Create your models here.
class Project(models.Model):
    """Model definition for Project."""

    # TODO: Define fields here
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img')

    class Meta:
        """Meta definition for Project."""

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
