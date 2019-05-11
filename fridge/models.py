import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    exp_date = models.DateTimeField(default=timezone.now)
    img = models.FileField(null=True)
    family_choices=(
        ("과일", '과일'),
        ("야채", '야채'),
        ("유제품", '유제품'),
        ("육류", '육류'),
        ("어류", '어류'),
        ("기타", '기타'),
    )
    family = models.CharField(
        choices = family_choices,
        default = "과일",
        max_length=200,
    )
    memo = models.TextField()
    tag_set=models.ManytoManyField('Tag', blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

class Copost(models.Model):
    cotitle = models.CharField(max_length=200)
    cocontents = models.TextField()

    def __str__(self):
        return self.cotitle
