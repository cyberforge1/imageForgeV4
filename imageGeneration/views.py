from django.shortcuts import render

from .models import Prompts


def prompts(request):
    '''Show all prompts'''
    prompts = Prompts.objects.all()
    context = {'prompts': prompts}
    return render(request, 'imageGeneration/prompts.html', context)
