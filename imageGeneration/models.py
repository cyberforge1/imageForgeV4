from django.db import models

# Create your models here.
class Prompts(models.Model):
    '''A prompt generated for the user'''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def get_text(self):
        return self.text_field
    
    def get_datetime(self):
        return self.datetime_field