
from playsound import playsound
from pygame import mixer
import glob	
import time

songs = glob.glob("C:\mutest\\*.mp3")


mixer.init()

for song in songs:
	mixer.music.load(song)
	mixer.music.set_volume(0.5)
	mixer.music.play()
	print("now playing "+song)
	while mixer.music.get_busy():
		pass