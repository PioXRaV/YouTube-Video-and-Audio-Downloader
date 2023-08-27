from pytube import YouTube

url = input("Enter the YouTube video URL.\n---> ")

yt = YouTube(url)

type = int(input("\n[1] Video\n[2] Audio\n---> "))

if type == 1 or type == 2:
	
	print("\nStream Selecting, Please Wait.")
	
	if type == 1:
		
		stream = yt.streams.get_highest_resolution()
		
	else:
		
		stream = yt.streams.filter(only_audio=True, file_extension="webm").order_by("abr").last()
	
	print("Downloading, Please Wait.")
	
	stream.download()

	print("\nDownloaded")