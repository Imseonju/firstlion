from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=10)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    def summary(self):
        return self.body[:2]