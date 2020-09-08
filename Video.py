import youtube_dl

# This is a test of the youtube_dl library on handling videos' song metada retrival
YT_URL= str(input("Put YT Video URL here: "))

ytRelevantData= youtube_dl.YoutubeDL({}) 

with ytRelevantData:
    video = ytRelevantData.extract_info(YT_URL,download=False)

print ('{} - {}'.format(video['artist'], video['track']))

class Video:

    def __init__(self, videoName, videoLink, videoSong):

        self.videoName = videoName
        self.videoLink = videoLink
        self.videoSong = videoSong

    def extractSong():

        """ 
        1. Pull relevant info out of YT API to construct 'song' obj
        
        """
