from django.db import models

# Create your models here.
class Prompts(models.Model):
    '''A prompt generated for the user'''
    text_field = models.TextField()  # Rename the field to avoid conflicts
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def get_text(self):
        return self.text_field
    
    def get_datetime(self):
        return self.date_added
    