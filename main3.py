import openai
import speech_recognition as sr
import pyttsx3

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
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('female', voices[1].id)
    engine.say(text)
    engine.runAndWait()

print('Hello! Let\'s chat.\n')
while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Speak:")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        myQn = r.recognize_google(audio)
        print("You said: " + myQn)
        response = generate_response(myQn)
        print(response + '\n')
        speak(response)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Sorry, I am unable to process your request at this time. Please try again later.")