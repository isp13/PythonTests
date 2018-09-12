import os
import webbrowser
from appJar import gui

def press(button):
    if button == "Cancel":
        app.stop()
        
    else:
    	webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

app = gui("Login Window", "500x300")
app.setBg("white")
app.addLabel("title", "А может да")
app.setFont(20)

app.addButtons(["да", "нет(да)","да в смысле нет"], press)

app.go()



import pyimgur

CLIENT_ID = "9a88d51bfff2779"
PATH = "/Users/nikita/Desktop/hackhack.png"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="hackhack")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)