from src import PDF, Voice, PII

import wave
import numpy as np


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
file_path = '/Users/haikux/Documents/projects/medley/assets/audio/sample.wav' 
with wave.open(file_path, 'rb') as wav_file:
    sample_rate = wav_file.getframerate()
    n_frames = wav_file.getnframes()
    duration = n_frames / sample_rate
    audio_data = wav_file.readframes(n_frames)

# Convert audio data to numpy array
audio = np.frombuffer(audio_data, dtype=np.int16)

vf = Voice()
print(vf.speech_to_text(audio))
"""

