import hashlib
from scipy.ndimage import maximum_filter
import librosa
import numpy as np
import matplotlib.pyplot as plt


class SignalProcessing():
    def __init__(self): 
        pass

    def FindHash():
        pass
        
    def LoadAudio():
        # Load audio
        y, sr = librosa.load("tokyo_ghoul_unravel.mp3", sr=22050)

        # Compute spectrogram
        S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))
        S_db = librosa.amplitude_to_db(S, ref=np.max)

        # Show spectrogram
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
        plt.colorbar()
        plt.title('Spectrogram (dB)')
        plt.tight_layout()
        plt.show()

    def get_peaks(S_db, threshold=10, neighborhood_size=20):
        # Find local maxima
        local_max = maximum_filter(S_db, size=neighborhood_size) == S_db
        detected_peaks = (S_db > threshold) & local_max
        peak_coords = np.argwhere(detected_peaks)

        return peak_coords  # (frequency_bin, time_bin)

    peaks = get_peaks(S_db)
    print(f"Found {len(peaks)} peaks.")

    def generate_hashes(peaks, fan_value=5):
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

    fingerprints = generate_hashes(peaks)
    print(f"Generated {len(fingerprints)} hashes.")


    db = {}  # Simulated database

    # Store: song title → hashes
    def store_song(title, fingerprints):
        for h, t in fingerprints:
            if h not in db:
                db[h] = []
            db[h].append((title, t))

    store_song("tokyo_ghoul_unravel", fingerprints)

    def match_clip(fingerprints):
        matches = {}
        for h, t in fingerprints:
            if h in db:
                for song_title, song_time in db[h]:
                    delta = song_time - t
                    matches[(song_title, delta)] = matches.get((song_title, delta), 0) + 1

        if matches:
            best_match = max(matches, key=matches.get)
            print(f"Best match: {best_match[0]} (score: {matches[best_match]})")
        else:
            print("No match found.")

    # Load a short clip and repeat the process
    y_clip, _ = librosa.load("clip.wav", sr=22050)
    S_clip = np.abs(librosa.stft(y_clip, n_fft=2048, hop_length=512))
    S_db_clip = librosa.amplitude_to_db(S_clip, ref=np.max)
    peaks_clip = get_peaks(S_db_clip)
    fp_clip = generate_hashes(peaks_clip)

    match_clip(fp_clip)