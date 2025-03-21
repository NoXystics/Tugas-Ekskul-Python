import tkinter as tk
import pyttsx3
from tkinter import ttk

window = tk.Tk()
window.title('Text To Speech App')
window.geometry('400x300')

def text_to_speech():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties before adding anything to speak
    speed = int(speed_.get())
    engine.setProperty('rate', speed)
    
    volume = engine.getProperty('volume')  # Get current volume
    print(f"Current volume: {volume}")
    volume = float(volume_.get())
    engine.setProperty('volume', volume)

    # Convert text to speech
    speed = engine.getProperty('rate')  # Get current speed
    print(f"Current speed: {speed}")
    textspeech = entry.get()  # Get the text from the entry widget
    # Set properties before adding anything to speak
    engine.say(textspeech)
    
    # Wait for the speech to finish
    engine.runAndWait()
    engine.stop()  # Stop the engine after speaking
    
def volume_changed(value):
    volume_string.set(f"Volume: {value}")

def speed_changed(value):
    speed_string.set(f"Speed: {value}")


# Label title
title_label = ttk.Label(window, text ='Text To Speech App', font ='Times 26 bold')
title_label.pack()

input_frame = ttk.Frame(window)

# Input text field
entry_String = tk.StringVar()
entry = ttk.Entry(input_frame, textvariable = entry_String)
button = ttk.Button(input_frame, text ='Speak',command = text_to_speech)
input_frame.pack(pady = 10)
entry.pack(side ='left',padx = 10)
button.pack(side ='left')

# Volume setting
volume_ = ttk.Scale(from_=0.0, to=1.0, orient='horizontal', command=volume_changed)
volume_.pack()
volume_label = ttk.Label(window, text='Set Volume (0 to 1): ')
volume_label.pack()

# Volume label
volume_string = tk.StringVar()
volume_label = ttk.Label(window, text ='Volume', font ='Calibri 26 bold', textvariable = volume_string)
volume_label.pack(pady=5)

# Speed setting
speed_ = ttk.Scale(from_=50, to=200, orient='horizontal', command=speed_changed)
speed_.pack()
speed_label = ttk.Label(window, text='Set Speed (words per minute):')
speed_label.pack()

# Volume label
speed_string = tk.StringVar()
speed_label = ttk.Label(window, text ='Speed', font ='Calibri 26 bold', textvariable = speed_string)
speed_label.pack(pady=5)

# Run the application
window.mainloop()
