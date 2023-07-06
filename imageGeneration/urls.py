'''Defines URL patterns for imageGeneration.'''

from django.urls import path


# Additions to fetch an image
from django.conf import settings

from . import views

app_name = 'imageGeneration'

urlpatterns = [
    # Prompts
    path('prompts/', views.prompts, name='prompts'),
]