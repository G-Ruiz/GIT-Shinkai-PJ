class YTlist:

    def __init__(self, listName, videoInList, listLink):

        self.listName = listName
        self.videoInList = videoInList
        self.listLink = listLink



    def populateList(listLink):

        '''
        
        1. here goes the call to youtoube API to link all the videos in the list to the object YTList
        
        2. When the method receive the videos it should relate the object video to the object YTList thru a
        a object "VideoInList"

        3. The method finishes with the append onf the VideoInList object to in a list on 'videoInList' parameter on the YTList object

        '''