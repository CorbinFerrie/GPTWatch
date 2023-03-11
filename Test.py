import gradio as gr


def transcribe(audio):
    print(audio)
    return 'text'

gr.Interface(
    fn=transcribe, 
    inputs=gr.inputs.Audio(source="microphone", type="filepath"), 
    outputs="text").launch()