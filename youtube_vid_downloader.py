from pytube import Youtube
link = "#insert any link here"
yt = Youtube(link)
yt.streams.first().download()