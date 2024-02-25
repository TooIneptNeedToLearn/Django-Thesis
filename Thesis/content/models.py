from django.db import models
from django.utils.text import slugify

class Thesis(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  
    authors = models.CharField(max_length=100)
    abstract = models.TextField()
    panelist = models.CharField(max_length=100)
    advisors = models.CharField(max_length=255)
    department = models.CharField(max_length=100)  
    defense_date = models.DateField()
    published_date = models.DateField()
    keywords = models.CharField(max_length=255)
    status = models.CharField(
        max_length=2,
        choices=[
            ("RJ", "Rejected"),
            ("PB", "Published"),
            ("UR", "Under Review"),
        ],
        default="UR"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)
