'''from moviepy.editor import *

clip = VideoFileClip(r'H:\vaibhav\PycharmProjects\Automation_video\clip\01.mp4')

w,h = clip.size

print(w, h)

print(clip.duration/60)

clip2 = clip.subclip( t_end=(0, 0, 15))

clip2.write_videofile(r'H:\vaibhav\PycharmProjects\Automation_video\clip\01_clipped.mp4')'''


from moviepy.editor import *

audioclip = AudioFileClip(r"H:\vaibhav\PycharmProjects\Automation_video\clip\audio.mp3")
t=audioclip.duration
img = [r'H:\vaibhav\PycharmProjects\Automation_video\clip\1.jpg']
clips = [ImageClip(m).set_duration(t)
      for m in img]


concat_clip = concatenate_videoclips(clips, method="compose")

videoclip = concat_clip.set_audio(audioclip)




cat = (ImageClip(r"H:\vaibhav\PycharmProjects\Automation_video\clip\2.png")
           .set_start(2) #which second to start displaying image
           .set_duration(t-2) #how long to display image
           .set_position(("center", "center")))


videoclip = CompositeVideoClip([videoclip, cat])

cat = (ImageClip(r"H:\vaibhav\PycharmProjects\Automation_video\clip\3.png")
           .set_start(7) #which second to start displaying image
           .set_duration(t-7) #how long to display image
           .set_position(("center", "center")))

videoclip = CompositeVideoClip([videoclip, cat])

cat = (ImageClip(r"H:\vaibhav\PycharmProjects\Automation_video\clip\4.png")
           .set_start(14) #which second to start displaying image
           .set_duration(t-14) #how long to display image
           .set_position(("center", "center")))


videoclip = CompositeVideoClip([videoclip, cat])


videoclip.write_videofile("test.mp4", fps=24)

