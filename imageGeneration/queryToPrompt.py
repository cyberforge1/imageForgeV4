from imageGeneration.models import Prompts
from imageGeneration.createQuery import generatePrompt
from datetime import datetime

def generatePromptInstance():
    new_prompt = Prompts()
    new_prompt.text = generatePrompt()
    new_prompt.date_added = datetime.now()
    new_prompt.save()
    print(new_prompt.get_text())
    print(new_prompt.get_datetime())
    
generatePromptInstance()
    
