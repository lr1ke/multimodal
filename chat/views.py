from django.shortcuts import render
from django.http import JsonResponse
from .story_generator import generate_story

def generate_story_from_snippets(request):
    words = request.GET.get('words') # Extract the expected phrases from the request
    story = generate_story(words) # Call the generate_story function with the extracted phrases
    return JsonResponse({'story': story}) # Return the story as a JSON response

