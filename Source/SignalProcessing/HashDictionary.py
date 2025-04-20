import hashlib
import json

FULL_SONG_1 = "Source/Database/MusicData/FirstKiss.mp3"
FULL_SONG_2 = "Source/Database/MusicData/SayYes.mp3"
FULL_SONG_3 = "Source/Database/MusicData/Codeop4.mp3"
CLIP_1 = "Source/Database/Clip/Clip1.mp3"
CLIP_2 = "Source/Database/Clip/Clip2.mp3"
CLIP_3 = "Source/Database/Clip/Clip3.mp3"

HASH_FILE = "Source/Database/MusicHashes/hashes.json"

database = {}

hashes = {
        "abdsf" : 12,
        "abdsf" : 12,
    }

class HashDictionary():
    
    # Store: song title → hashes
    def StoreSong(self, songId, fingerprints):
        hashes = {}
        songArray = ["","","","","",""]
        
        for h, t in fingerprints: 
            if h not in hashes:
                database[h] = []
            hashes[h].append(t)
            
            dataTemp = self.AddToJson(songId, songArray, hashes)
            
            with open(HASH_FILE, "w") as file:
                json.dump(dataTemp, file, indent = 4)
                
    def AddToJson(self, songId, songArray, hashes):
        dataTemp = {}
        
        # Add to database
        dataTemp[str(songId)] = {
            "Anime"   : songArray[0],
            "Type"    : songArray[1],
            "Song"    : songArray[2],
            "Artist"  : songArray[3],
            "Composer": songArray[4],
            "Arranger": songArray[5],
            "hashes"  : hashes
        }
        
        return dataTemp