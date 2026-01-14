from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(
       
        blank=True,
        null=True
    )
    headline = models.CharField(max_length=150, blank=True)  # <-- NEW
    objective = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class TechnicalSkill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Links(models.Model):
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return "Social Links"
