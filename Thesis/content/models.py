from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

class Thesis(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True
                            ,unique_for_date = "published_date")  
    authors = models.CharField(max_length=100)
    abstract = models.TextField()
    body = models.TextField()
    panelist = models.CharField(max_length=100)
    advisors = models.CharField(max_length=255)
    department = models.CharField(max_length=100)  
    defense_date = models.DateField()
    published_date = models.DateField(default=timezone.now)
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

    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['-published_date'])
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('content:thesis_details', args=[self.published_date.year, self.published_date.month,self.published_date.day,self.slug])
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)
