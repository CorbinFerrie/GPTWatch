import openai
from gtts import gTTS
from tempfile import TemporaryFile
import pygame

def generate_response(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens= 450,
    )
    return response.choices[0].text

def speak(text):
    tts = gTTS(text=text, lang='en')
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    tts.speed = 25
    while pygame.mixer.music.get_busy():
        continue
    f.close()

print('Hello! Let\'s chat.\n')
while True:
    myQn = input()
    response = generate_response(myQn)
    print(response + '\n')
    speak(response)