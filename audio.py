import pyaudio
import wave
import keyboard

# Set up the audio stream
chunk = 1024  
sample_format = pyaudio.paInt16  
channels = 2  
fs = 44100  
filename = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

# Record the audio when 'p' is pressed
frames = []
recording = True

def start_recording():
    global recording
    recording = True

def stop_recording():
    global recording
    recording = False

keyboard.add_hotkey('p', start_recording)
keyboard.add_hotkey('ctrl+alt+shift+p', stop_recording)

while True:
    if recording:
        data = stream.read(chunk)
        frames.append(data)

    if keyboard.is_pressed('p'):
        break

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