'''
author: AbdAlMoniem AlHifnawy
author's email: hifnawy_moniem@hotmail.com
file name: rename_subtitles.py
date created: 13 Mar 2018 05:32 AM
description: this program rename subtitles of movies and series in a given folder path,
				the subtitles must be named in the same order as the videos
				i.e. if subs file names are 1, 2, 3, 4, 5... and videos file names are a, b, c, d, e...
				then video a gets sub 1, b 2, c 3, d 4, e 5 and so on...
'''

import os
import sys

# an array containing all possible video format extensions
videosExtensions = []

# an array containing all possible subtitle format extensions
subtitlesExtensions = []

'''
renames subtitles to their respective video name

arguments:
	@path: the path of the folder contating subtitles and videos
	@settingsPath: the path of the configuration file (settings.conf)
return:	nothing
'''
def main(path, settingsPath):
	print "Current path:", path
	
	# read the configuration file to get all file extensions	
	readConfigurationFile(settingsPath)

	# list the files and directories that are inside the @path directory
	files = os.listdir(path)

	# an array to hold the names of all videos inside the @path directory
	videos = []

	# an array to hold the names of all subtitles inside the @path directory
	subtitles = []
	
	# loop through the files and directories inside the @path directory and extract the videos and subtitles
	for file in files:
		# extract the file name and extension
		fileName, fileExtension = getFileExtension(file)
		
		# if the file's extension is a video extension, add to the @videos array
		if fileExtension in videosExtensions:
			videos.append(file)
			continue
		
		# if the file's extension is a video extension, add to the @subtitles array
		if fileExtension in subtitlesExtensions:
			subtitles.append(file)
			continue

	print "\nVideos:"
	for video in videos:
		print video
	print
	
	print "Subtitles:"
	for sub in subtitles:
		print sub
	print

	# if no videos are found, exit the program
	if len(videos) < 1:
		print "Error: No video files found!"
		pause(2)
	
	# if no subtitles are found, exit the program
	if len(subtitles) < 1:
		print "Error: No subtitle files found!"
		pause(3)

	# if the number of videos doesn't match the number of subtitles, exit the program
	if len(videos) != len(subtitles):
		print "Error: Number of subtitles and videos doesn't match!"
		pause(4)
	else:
		i = 0
		path += "\\"

		renamedAFile = False
		filesRenamed = 0

		# rename the subtitles files to their respective video name
		while i < len(videos):
			videoFile = videos[i]
			subtitleFile = subtitles[i]
			
			# extract the video file name and extension
			videoFileName, videoFileExtension = getFileExtension(videoFile)
			
			# extract the subtitle file name and extension
			subtitleFileName, subtitleFileExtension = getFileExtension(subtitleFile)
			
			if subtitleFileName != videoFileName:
				print "Renaming \"%s\" to \"%s\"\n" %(subtitleFile, "%s.%s" %(videoFile, subtitleFileExtension))

				# add the full path to the video file name
				videoFile = path + videoFileName

				# add the full path to the subtitle file name
				subtitleFile = path + subtitleFile

				# rename the subtitle file to the video file name with the subtitle file's extension
				os.rename(subtitleFile, "%s.%s" %(videoFile, subtitleFileExtension))

				renamedAFile = True
				filesRenamed += 1

			i += 1

		if renamedAFile:
			print "%d %s renamed." %(filesRenamed, "file" if filesRenamed == 1 else "files")
		else:
			print "no files were renamed, all subtitles are the same name."

'''
reads a configuration file and fills in the @videosExtensions array and the @subtitlesExtensions array

arguments:
	@file:	the path of the configuration file
return:	nothing
'''
def readConfigurationFile(file):
	print "Reading settings file..."
	
	settingsFile = open(file, 'r')
	
	videos = False
	for line in settingsFile:
		line = line.rstrip()
		
		# print line
		
		if line.lower() == "video formats:":
			videos = True
			continue

		if line.lower() == "subtitle formats:":
			videos = False
			continue

		if len(line) >= 1:
			if videos:
				videosExtensions.append(line)
			else:
				subtitlesExtensions.append(line)

	settingsFile.close()
	print "Video file extensions:", videosExtensions
	print "Subtitle file extensions:", subtitlesExtensions

'''
gets the extension of a given file

arguments:
	@file:	the file to extract extension from
return:
	a tuble containing the file name without the extension and the extension
'''
def getFileExtension(file):
	fileName, fileExtension = os.path.splitext(file)
	brokenFileName = fileExtension.split('.')
	fileExtension =  brokenFileName[1] if len(brokenFileName) > 1 else fileExtension
	return (fileName, fileExtension)

'''
was used to pause the code for debugging purposes, now just exits the program with a given exit code

arguments:
	@code: the exit code of the program
return:	nothing
'''
def pause(code = 0):
	exit(code)

	# while True:
	# 	pass

if __name__ == '__main__':
	# check if the program received a second argument
	# TODO: should add path checking...
	if len(sys.argv) != 2:
		print "Usage: %s <folder path>" %sys.argv[0]
		pause(1)

	# the configuration file is currently located in the same directory of this script and is called 'settings.conf'
	settingsPath = sys.path[0] +  "\\" + "settings.conf"
	
	# the path is the first command line argument to the program
	path = sys.argv[1]
	
	# execute the renaming algorithm
	main(path, settingsPath)