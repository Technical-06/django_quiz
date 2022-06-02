from django.db import models

class Quiz(models.Model):
    id=models.IntegerField(primary_key=True)
    question1 = models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    corrans=models.CharField(max_length=100)
    class Meta:
        db_table ="quiz"
