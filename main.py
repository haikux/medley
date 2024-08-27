from src import PDF, Voice, PII

import wave
import numpy as np
from io import BytesIO
import requests
import base64


#df = PDF("/Users/haikux/Documents/projects/medley/Sample.pdf")
#print(df.get_metadata())

#print(df.read_all())

#print(df.read_page(0, save_images=False))

"""
#Anonymize Texts

pii = PII()
text = "John Smith drivers license is AC432223"
resp = pii.analyze(text)
res = pii.anonymize(text, resp)

"""

"""
# Load and transcribe audio files
"""
file_path = '/Users/haikux/Documents/projects/medley/assets/audio/sample2.wav' 
with wave.open(file_path, 'rb') as wav_file:
    sample_rate = wav_file.getframerate()
    n_frames = wav_file.getnframes()
    duration = n_frames / sample_rate
    audio_data = wav_file.readframes(n_frames)

# Convert audio data to numpy array
audio = np.frombuffer(audio_data, dtype=np.int16)
audio_bytes = audio.tobytes()

url = 'http://localhost:5003/speech-to-text'
data = {'audio': base64.b64encode(audio_bytes).decode("utf-8"), 'sampling_rate': str(sample_rate), 'target_lang': 'eng', 'pii_mask': 'false'}
response = requests.post(url, data=data)

print("resp: ",response.text)

