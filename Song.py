'''

- The 'videoList' attribute refers to on which videos this particular song is cointained

'''

class Song:

    def __inti__(self, songName, songArtist, songLink, videoList):

        self.songName = songName
        self.songArtist = songArtist
        self.songLink = songLink
        self.videoList = videoList
