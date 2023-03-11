import gradio as gr
import openai, subprocess
openai.api_key = "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"

messages = [{"role": "assistant", "content": 'You are an assistant. Respond to all input in 100 words or less.'}]

def transcribe(audio):
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
    return(chat_transcript)

ui = gr.Interface(
    fn=transcribe, 
    inputs=gr.inputs.Audio(source="microphone", type="filepath"), 
    outputs="text").launch()

ui.launch()