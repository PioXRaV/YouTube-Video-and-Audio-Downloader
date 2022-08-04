from pytube import YouTube

url = input("Enter the YouTube video URL.\n---> ")

video = YouTube(url)

options = video.streams

print()

for i in options:

    print(i)

itag = int(input("\nEnter the itag number.\n---> "))

video.streams.get_by_itag(itag).download()

print("\nDownloaded")