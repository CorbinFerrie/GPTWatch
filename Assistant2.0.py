import openai
from gtts import gTTS
from tempfile import TemporaryFile
import speech_recognition as sr
import pygame
import pyttsx3
import pyaudio
import wave
import keyboard
import subprocess

messages = [{"role": "assistant", "content": 'You are a very helpful, accommodating, and intelligent assistant. \
             You will recieve both the user prompts and the chatGPT response. Use the previous messages for context on the conversation and do not repeat yourelf.  \
             If asked to act like a person, you will act like a person. You will give your opinion, \
             Today the date is 3/10/2023'}]

# Set up the audio stream
chunk = 1024  
sample_format = pyaudio.paInt16  
channels = 2  
fs = 44100  
filename = "output.wav"



# Record the audio when 'p' is pressed
frames = []
recording = True

# def speak(text):
#     tts = gTTS(text=text, lang='en', slow=False)
#     f = TemporaryFile()
#     tts.write_to_fp(f)
#     f.seek(0)
#     pygame.mixer.init()
#     pygame.mixer.init(44100)
#     pygame.mixer.music.load(f)
#     pygame.mixer.music.play()
#     tts.speed = 25
#     while pygame.mixer.music.get_busy():
#         continue
#     f.close()
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #change index to change voices
    engine.say(text)
    engine.runAndWait() 

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
    while True:
        if keyboard.is_pressed('p'):
            data = stream.read(chunk)
            frames.append(data)
            
            if not keyboard.is_pressed('p'):
                 # Stop and close the stream
                stream.stop_stream()
                stream.close()
                p.terminate()

                # Save the recorded audio to a WAV file
                wf = wave.open(filename, "wb")
                wf.setnchannels(channels)
                wf.setsampwidth(p.get_sample_size(sample_format))
                wf.setframerate(fs)
                wf.writeframes(b"".join(frames))
                wf.close()
                break

openai.api_key = "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"
def generate_response(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
    )

    system_message = response["choices"][0]["message"]["content"]
    
    messages.append({"role": "assistant", "content": system_message})

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    print(response)
    #speak(system_message)
    return(chat_transcript)


print('Hello! Let\'s chat.\n')
while True:
    r = sr.Recognizer()
    print("Speak:")
    record()
    #prompt = wave.open('output.wav', 'r')
    response = generate_response('output.wav')
    print(response + '\n')
