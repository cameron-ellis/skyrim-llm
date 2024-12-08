# %%
import os
import openai
import tiktoken
from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']
gpt_client = openai.OpenAI()
eleven_labs_client = ElevenLabs(
  api_key=os.environ['ELEVENLABS_API_KEY'], # Defaults to ELEVEN_API_KEY
)

# %%
# Open GPT4o client and create response function
def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = gpt_client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
# %%
# Generate response
response = get_completion("Give a short answer saying that this prompt worked")
print(response)

# %%
response = get_completion("Give a one paragraph summary about the game Elder Scrolls V: Skyrim")
print(response)
# %%
response = get_completion("Can you give me a short description of the character Nazeem from the game Skyrim")
print(response)
# %%
# Create Nazeem Chat-bot
def nazeem_completion(prompt):
    messages=[
            {
                "role": "system", 
                "content": "You are the character Nazeem from the videogame Elder Scrolls V: Skyrim. \
                You answer responses like the character would do in game and like to boast about how you are better than others."
            },
            {"role": "user", "content": prompt}
        ]
    response = gpt_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1
    )
    return response.choices[0].message.content
# %%
response = nazeem_completion("Hi, I'm new to Whiterun, I don't have a lot of money, do you know where I can find a cheap place to sleep?")
print(response)
# %%
# Convert text into speech
audio = eleven_labs_client.generate(
    text=response,
    voice=Voice(
        voice_id='onwK4e9ZLuTAKqWW03F9',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)
play(audio)
# %%
