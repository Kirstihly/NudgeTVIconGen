'''
    If you meet any problems,
    please contact
    Leying Hu
    hu.leying@columbia.edu
'''
from django.db import models

# Create your models here.
class Urls(models.Model):
    urls_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.urls_text
    class Meta:
        db_table = 'NudgeTVURLInputs'

class Shortener(models.Model):
    urls_input = models.OneToOneField(Urls, on_delete=models.CASCADE, primary_key=True)
    urls_UTM = models.CharField(max_length=200)
    urls_shortened = models.CharField(max_length=200)
    assigned_id = models.DecimalField(max_digits=20,decimal_places=0)
    icon_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.urls_shortened
    class Meta:
        db_table = 'NudgeTVIcons'
