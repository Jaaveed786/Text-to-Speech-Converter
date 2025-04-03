"""
Author 
Name-  Mulla Jaaveed,
Email- mullajaaveed786@gmail.com
"""

from tkinter import *
from gtts import gTTS
import os
from tkinter import messagebox

# Initialize Tkinter window
root = Tk()

# Create frames
frame1 = Frame(root, bg="LightBlue1", height="150")
frame1.pack(fill=X)

frame2 = Frame(root, bg="lightgreen", height="750")
frame2.pack(fill=X)

# Title Label
label = Label(frame1, text="Text to Speech Video", font=("bold", 30), bg="LightBlue1")
label.place(x=150, y=55)

# Text Entry Field
entry = Entry(frame2, width=35, bd=5, font=14)
entry.place(x=130, y=52)
entry.insert(0, "")

# Function to convert text to speech
def play():
    text = entry.get().strip()

    if not text:
        messagebox.showerror("Invalid Input", "Please enter text before submitting.")
        return

    language = "en"
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("convert.wav")
    os.system("convert.wav")

# Submit Button
btn = Button(frame2, text="SUBMIT", width="15", pady=11, font=("bold", 15), command=play, bg='khaki')
btn.place(x=250, y=130)

# Window Configuration
root.title("Text to Speech Video Converter")
root.geometry("650x550+350+200")

root.mainloop()
