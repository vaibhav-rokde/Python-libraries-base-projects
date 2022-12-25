
# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import wget
import os
from pydub import AudioSegment  
import bs4
import requests
from selenium import webdriver

import time
import mechanicalsoup

from moviepy.editor import *


def audio(mytext, content):
    language = 'en'

    content = mytext + content
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobjcontent = gTTS(text=content, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    
    myobj.save("{}.mp3".format(mytext))
    myobjcontent.save("{}_content.mp3".format(mytext.replace(" ","_")))

    return myobj, myobjcontent

def downloadImages(mytext, content, count):
    

    browser = mechanicalsoup.StatefulBrowser()
    url = "https://www.google.com/imghp?hl=en"

    browser.open(url)
    print(browser.get_url())

    #get HTML
    browser.get_current_page()

    #target the search input
    browser.select_form()
    browser.get_current_form().print_summary()

    #search for a term
    search_term_name = mytext
    search_term = mytext + " " + "HD images through corporate industry peoples"
    browser["q"] = search_term 

    #submit/"click" search
    browser.launch_browser()
    response = browser.submit_selected()

    print('new url:', browser.get_url())
    print('my response:\n', response.text[:500])

    #
    new_url=browser.get_url()
    browser.open(new_url)


    ##### 
    page=browser.get_current_page()
    all_image=page.find_all('img')


    ###

    image_source=[]

    for image in all_image:
        image=image.get('src')
        image_source.append(image)


    image_source=[image for image in image_source if image.startswith('https')]
    print(image_source)

    folder_name = 'videoImages'
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

    path=os.getcwd()
    path=os.path.join(path, folder_name)

    c=0
    search_term_name=search_term_name.replace(" ","_")
    for image in image_source[:count]:
        save_as = os.path.join(path, search_term_name + str(c) + '.jpg')
        wget.download(image, save_as)
        c += 1

    return path

def videomaker(mytext, content, imagepath,count):
    file=mytext.replace(" ","_")

    audioclip = AudioFileClip("{}_content.mp3".format(file))

    new_audioclip = CompositeAudioClip([audioclip])

    t=audioclip.duration
    t1=int(t//9)
    print("time audio: ",t1)

    imagelst=[]
    clips=[]
    for i in range(0,count):
        imagelst.append(imagepath+'/'+ file +"{i}".format(i=i)+'.jpg')
        clip=ImageClip(imagelst[i]).set_duration(5)
        clips.append(clip)



    video_clip = concatenate_videoclips(clips, method='compose')
    #video_clip.set_audio(audioclip)

    video_clip.audio = new_audioclip
    video_clip.resize( (460,720) )
    video_clip.write_videofile("{}.mp4".format(file), fps=24, remove_temp=True, codec="libx264", audio_codec="aac")

    #creating a directory to save images
    return "done"


# The text that you want to convert to audio
mytext = '''Why networking is a long-term game'''
content = '''Networking isnot a task you should only prioritize when you are looking for work. Why, Because
building strong relationships takes time; The more energy you put into fostering your connections, the
more you will be able to mutually help each other throughout your careers. To engage your existing
network now so that they can help match you to future opportunities, Fast Company recommends
taking three steps:
 Discover who is hiring in your network to identify who can support your job hunt.
 Post online that you are looking for work (when ready) to activate your network.
 Refresh your skills to help you stand out among candidates.'''

myobj, myobjcontent = audio(mytext, content)
file=mytext.replace(" ","_")
audioclip = AudioFileClip("{}_content.mp3".format(file))
t=audioclip.duration
count=int(t//4)
imagepath = downloadImages(mytext, content,count)
out= videomaker(mytext, content, imagepath, count)
print(out)