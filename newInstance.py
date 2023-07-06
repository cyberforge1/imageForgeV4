import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'll_project.settings'
django.setup()


from imageGeneration.models import Prompts

from createQuery import generatePrompt


new_model = Prompts()

new_model.text_field = generatePrompt()

new_model.save()