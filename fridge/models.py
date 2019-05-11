
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    year_choices = (
        ("2019", "2019"),
        ("2020", "2020"),
        ("2021", "2021"),
        ("2022", "2022"),
        ("2023", "2023"),
    )
    month_choices = (
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
        ("6", '6'),
        ("7", '7'),
        ("8", '8'),
        ("9", '9'),
        ("10", '10'),
        ("11", '11'),
        ("12", '12'),
    )

    date_choices=(
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
        ("6", '6'),
        ("7", '7'),
        ("8", '8'),
        ("9", '9'),
        ("10", '10'),
        ("11", '11'),
        ("12", '12'),
        ("13", '13'),
        ("14", '14'),
        ("15", '15'),
        ("16", '16'),
        ("17", '17'),
        ("18", '18'),
        ("19", '19'),
        ("20", '20'),
        ("21", '21'),
        ("22", '22'),
        ("23", '23'),
        ("24", '24'),
        ("25", '25'),
        ("26", '26'),
        ("27", '27'),
        ("28", '28'),
        ("29", '29'),
        ("30", '30'),
        ("31", '31'),
    )

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
    date = models.CharField(
        choices = date_choices, 
        default = "1",
        max_length=200,
    )
    month = models.CharField(
        choices = month_choices, 
        default = "5",
        max_length=200,
    )
    year = models.CharField(
        choices = year_choices, 
        default = "2019",
        max_length=200,
    )
    memo = models.TextField()
    
    
    def __str__(self):
        return self.name



class Copost(models.Model):
    cotitle = models.CharField(max_length=200)
    cocontents = models.TextField()

    def __str__(self):
        return self.cotitle
