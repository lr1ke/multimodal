from django.urls import path
from .views import generate_story_from_snippets

urlpatterns = [ 
    # path('', index, name='index'),    
    # path('response', response, name='response'),
    path('generate-story-from-snippets/', generate_story_from_snippets, name='generate-story-from-snippets')
    
]
