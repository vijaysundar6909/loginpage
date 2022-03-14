from django.db import models

# Create your models here.


class subject(models.Model):
    gmail = models.EmailField(primary_key=True)
    english = models.IntegerField()
    tamil = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()

class detail(models.Model):
    username = models.CharField(max_length=100,null=True)
    gmail = models.ForeignKey(subject, on_delete=models.CASCADE)
    choose_section = (('+1','class11'),('+2','class12'))
    section = models.CharField(max_length=2,choices=choose_section)
    choose_gender = (('M', 'Male'),('F','Female'))
    gender = models.CharField(max_length=1,choices=choose_gender)

class rank(models.Model):
    gmail = models.ForeignKey(subject, on_delete=models.CASCADE)
    total = models.IntegerField()
    rank = models.IntegerField(null=True)

