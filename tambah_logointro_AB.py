import moviepy
import sys
import moviepy.editor as mp
import os


def add_intro(logoadded, introneeded=True):
	if introneeded==True:
		video = mp.VideoFileClip("introoutro.mp4")
		intro = video.subclip(0,8)
		outro = video.subclip(-10,video.duration)
		final = mp.concatenate([intro,logoadded,outro])
		return final
	else:
		return logoadded


def add_logo(videopath):
	logopath = "~/Downloads/Logo Ajarbelajar-03.png"
	videointrooutro = mp.VideoFileClip("introoutro.mp4")
	intro = videointrooutro.subclip(0,8)
	outro = videointrooutro.subclip(-10,videointrooutro.duration)
	video = mp.VideoFileClip(videopath)
	durationset=video.duration
	scale=intro.h / video.h
	video =  video.resize(scale)
	logo = mp.ImageClip(logopath).set_duration(durationset).resize(0.7).margin(left=0,top=0).set_position(("left","top"))
	final = mp.CompositeVideoClip([video.set_duration(durationset),logo])
	print("ok")	
	return final

def save_change(logointroadded):
	logointroadded.write_videofile("ABedit_"+sys.argv[1][:-5]+".mp4")






if __name__ == "__main__":
	logoadded = add_logo(sys.argv[1])
	save_change(add_intro(logoadded))
	print("sudah selesai")
	sys.exit(0)

