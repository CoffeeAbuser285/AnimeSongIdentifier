import hashlib
import json
import os
from scipy.ndimage import maximum_filter
import librosa
import numpy as np
import matplotlib.pyplot as plt
from .HashDictionary import HashDictionary

SONG_DIRECTORY = "Source/Database/MusicData"
CLIP_1 = "Source/Database/Clip/Clip1.mp3"
CLIP_2 = "Source/Database/Clip/Clip2.mp3"
CLIP_3 = "Source/Database/Clip/Clip3.mp3"

HASH_FILE = "Source/Database/MusicHashes/hashes.json"

database = {}

class SignalProcessing(HashDictionary):
    
    # Populate Hash File with songs from folder
    def PopulateHashFile(self):
        mp3Files = []
        titles = []
        
        # Finding all songs in folder
        for filename in os.listdir(SONG_DIRECTORY):
            if filename.lower().endswith(".mp3"):
                mp3Files.append(os.path.join(SONG_DIRECTORY, filename))
                titles.append(filename)
                
        # Storing songs into database
        for title, mp3 in zip(titles, mp3Files):
            S_db         = self.LoadAudio(mp3)
            peaks        = self.GetPeaks(S_db)
            fingerprints = self.GenerateHashes(peaks)
            self.TempStoreSong(title, fingerprints)
        
    # Grabbing Song Information
    def GetSongInformation(self):
        #TODO: Replace clip with real time audio
        S_db        = self.LoadAudio(CLIP_2)
        peaks        = self.GetPeaks(S_db)
        fingerprints = self.GenerateHashes(peaks)
        songArray    = self.MatchClip(fingerprints)
        
        print(f"Found {len(peaks)} peaks.")
        print(f"Generated {len(fingerprints)} hashes.")
        
        return [songArray, "", "", "", "", "", ""]
        
    def TempStoreSong(self, title, fingerprints):
        for h, t in fingerprints:
            if h not in database:
                database[h] = []
            database[h].append((title, t))
    
    def LoadAudio(self, song):
        # Load audio
        y, sr = librosa.load(song, sr=22050)

        # Compute spectrogram
        # Frames = 22050 (sr) / 512 (hop length)
        S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))
        S_db= librosa.amplitude_to_db(S, ref=np.max)

        return S_db
        

    def GetPeaks(self, S_db, threshold=-20, neighborhood_size=20):
        # Find local maxima
        local_max = maximum_filter(S_db, size=neighborhood_size) == S_db
        detected_peaks = (S_db > threshold) & local_max
        peak_coords = np.argwhere(detected_peaks)
        
        '''
        for i in peak_coords:
            print(i)
        '''

        return peak_coords  # (frequency_bin, time_bin)

    def GenerateHashes(self, peaks, fan_value=5):
        hashes = []
        for i in range(len(peaks)):
            for j in range(1, fan_value):
                if i + j < len(peaks):
                    freq1 = peaks[i][0]
                    time1 = peaks[i][1]
                    freq2 = peaks[i + j][0]
                    time2 = peaks[i + j][1]

                    t_delta = time2 - time1
                    if 0 < t_delta <= 200:
                        hash_input = f"{freq1}|{freq2}|{t_delta}"
                        h = hashlib.sha1(hash_input.encode("utf-8")).hexdigest()[0:20]
                        hashes.append((h, time1))
        return hashes

    def MatchClip(self, fingerprints):
        matches = {}
        for h, t in fingerprints:
            #TODO: match with the json
            if h in database:
                for song_title, song_time in database[h]:
                    delta = song_time - t
                    matches[(song_title, delta)] = matches.get((song_title, delta), 0) + 1

        if matches:
            best_match = max(matches, key=matches.get)
            print(f"Best match: {best_match[0]} (score: {matches[best_match]})")
            return song_title
        else:
            print("No match found.")
            return "match not found!"