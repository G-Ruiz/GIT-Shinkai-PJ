'''
*New Note for Commit Prooving*

import YTList
import ListVideo
import Video
import Song
import SPList

1. Request the YTList link. 
   1.1. Get Playlist relevant info.
2. Request individual video from YTList relevant info.
3. Look out for the song of the video
4. Create SPList
5. Append song to SPList
'''

def MainMenu():

    userSelection = 0

    while userSelection != 1 and userSelection != 2: 
        
        try: userSelection = int(input("\nMain menu\n\nPick an option:\n\n1. to create a new playlist\n2. Exit\n").strip())
        
        except ValueError: print("\nNot a Number!")

        
        if userSelection == 1 : 
        
            ConvertYTPlaylist()

        elif userSelection == 2:

            print("\nBye!")
            quit()
        
        else:
            
            print("\nTry again!")

def ConvertYTPlaylist():

    while True:
        
        YTPlayListLink = str(input("\nEnter the Playlist link \nor press 2 to go back to Main Menu\n").strip())

        if YTPlayListLink == "2":
            MainMenu() 
            

        elif "https://www.youtube.com/playlist?list=" not in YTPlayListLink: 

            print("\nThe input is not valid")

            continue

        else:
            
            # yTList = YTList().populate(YTPlayListLink)
            print("\nla buena!") #Aquí tenemos que seguir con el código...



if __name__ == '__main__':
    
    MainMenu()
    



