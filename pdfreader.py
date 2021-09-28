from tkinter import Tk 
from tkinter.filedialog import askopenfilename
import pyttsx3
import PyPDF3


Tk().withdraw() # Prevent Tkinter's window pop up  

# Open  window for file selection 
file = askopenfilename()


# allow user to select file
pdfreader = PyPDF3.PdfFileReader(file)

# Read the number of pages in the file
pages = pdfreader.numPages

 #read all pages 
for no in range(0,pages):
	page = pdfreader.getPage(no)
	text = page.extractText()
	engine = pyttsx3.init()
	engine.setProperty("rate", 140)
	new_vol = 8  # volume between 0 and 1
	engine.setProperty("volume", new_vol)
	engine.say(text)

# Save the audio in an mp3 fileformat

engine.save_to_file(text, 'myaudio.mp3')
engine.runAndWait()
