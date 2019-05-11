
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    year_choices = (
        ("2015년", "2015년"),
        ("2016년", "2016년"),
        ("2017년", "2017년"),
        ("2018년", "2018년"),
        ("2019년", "2019년"),
    )
    month_choices = (
        ("1월", '1월'),
        ("2월", '2월'),
        ("3월", '3월'),
        ("4월", '4월'),
        ("5월", '5월'),
        ("6월", '6월'),
        ("7월", '7월'),
        ("8월", '8월'),
        ("9월", '9월'),
        ("10월", '10월'),
        ("11월", '11월'),
        ("12월", '12월'),
    )

    date_choices=(
        ("1일", '1일'),
        ("2일", '2일'),
        ("3일", '3일'),
        ("4일", '4일'),
        ("5일", '5일'),
        ("6일", '6일'),
        ("7일", '7일'),
        ("8일", '8일'),
        ("9일", '9일'),
        ("10일", '10일'),
        ("11일", '11일'),
        ("12일", '12일'),
        ("13일", '13일'),
        ("14일", '14일'),
        ("15일", '15일'),
        ("16일", '16일'),
        ("17일", '17일'),
        ("18일", '18일'),
        ("19일", '19일'),
        ("20일", '20일'),
        ("21일", '21일'),
        ("22일", '22일'),
        ("23일", '23일'),
        ("24일", '24일'),
        ("25일", '25일'),
        ("26일", '26일'),
        ("27일", '27일'),
        ("28일", '28일'),
        ("29일", '29일'),
        ("30일", '30일'),
        ("31일", '31일'),
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
        default = "1일",
        max_length=200,
    )
    month = models.CharField(
        choices = month_choices, 
        default = "1월",
        max_length=200,
    )
    year = models.CharField(
        choices = year_choices, 
        default = "2019년",
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
