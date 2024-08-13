import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_KEY"])

def generate_story(words):
    # Call the OpenAI API to generate the story
    response = get_short_story(words)
    # Format and return the response
    return format_response(response)

def get_short_story(words):
    # Construct the system prompt
    system_prompt = f"""You make diary entries more cohesive.
    Take the following snippets: {words}. Write in the 'spontaneous prose' style.
    Don't add any new information, just make the existing information cohesive.
    Do not go beyond 50 tokens."""
    # Make the API call
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": system_prompt
        }],
        temperature=0.1,
        max_tokens=50
    )

    # Return the API response
    return response

def format_response(response):
    # Extract the generated story from the response
    story = response.choices[0].message.content
    # Remove any unwanted text or formatting
    story = story.strip()
    # Return the formatted story
    return story

# print(generate_story("cat is sleeping, I'm reading book, computer muted, grizzly sun, i need water"))