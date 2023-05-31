import tkinter as tk
import sounddevice as sd
import pyttsx3
import openai
from scipy.io.wavfile import write
# import os # See line 50

engine = pyttsx3.init()
fs = 44100  # Sample rate
seconds = 8  # Duration of recording

def save_api():
    openai.api_key = api_entry.get()

def start_recording():
    record_button.config(state='disabled')
    
    # Start recording
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    
    write('output.wav', fs, recording)  # Save Recording

    audio_file = open('output.wav', 'rb')
    response = openai.Audio.transcribe("whisper-1", audio_file)

    # Assume the response returns the transcribed audio in text format
    transkribiertes_audio = response['text']
    print ("Transkript: "+transkribiertes_audio) # For debug only

    # Send the transcribed audio to ChatGPT
    temperature = 0.5 # "Craziness" of response (0 (technical) to 1 (crazy)), 0.5 default)
    prompt = transkribiertes_audio
    chat_gpt_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000, # Length of response, 150 default
        n=1,
        stop=None,
        temperature=temperature,
        top_p=1
    )

    message = chat_gpt_response.choices[0].text.strip()
    print ("Antwort ChatGPT: "+message) # For debug only

    # Play the response from ChatGPT
    play_response(message)
    
    # Delete the audio file
    # os.remove('output.wav')
    # commented out because threw error considering writing rights

    record_button.config(state='normal')

def play_response(response):
    engine.say(response)
    engine.runAndWait()

root = tk.Tk()
root.title("OpenAI Whisper und ChatGPT Anwendung")

api_entry = tk.Entry(root)
api_entry.pack()

save_button = tk.Button(root, text="Speichern", command=save_api)
save_button.pack()

record_button = tk.Button(root, text="Aufnahme", command=start_recording, state='normal')
record_button.pack()

root.mainloop()
