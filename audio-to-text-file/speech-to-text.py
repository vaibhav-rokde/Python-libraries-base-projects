#import library
import speech_recognition as sr
import time

#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
with sr.AudioFile('test.wav') as source:
    audio_text = r.listen(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
        time1 = time.strftime("%H_%M_%S")
        text_file = open("output_data_{time1}.txt".format(time1=time1), "w")
        text_file.write(text)
        text_file.close()
        print('done')
    except:
         print('Sorry.. run again...')