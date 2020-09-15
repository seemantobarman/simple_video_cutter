from tkinter import Tk
from tkinter.filedialog import askopenfilename,askdirectory
import ntpath
from moviepy.editor import VideoFileClip

def timeConverter(time):
    (h,m,s) = time.split(':')
    result = int(h)*3600 + int(m)*60 + int(s)
    return result

Tk().withdraw()
filename = askopenfilename()

extension = "mp4"
if filename[-3:]==extension:
    start = input("Entar the starting position (h:m:s): ")
    start = timeConverter(start)

    end = input("Entar the ending position (h:m:s): ")
    end = timeConverter(end)

    if start<end:
        result_file = ntpath.basename(filename)
        index = result_file.find(".mp4")
        result_file = result_file[:index] +" (Edited)"+result_file[index:]

        dir_of_new_file = askdirectory()
        total_filepath = dir_of_new_file +"/" +result_file

        clip = VideoFileClip(filename).subclip(start,end)
        clip.to_videofile(total_filepath, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    else:
        print("\nInitial starting position should be less then ending position")
else:
    print("Please select a mp4 file")

