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
vf = Voice()
file_path = '/Users/haikux/Documents/projects/medley/assets/audio/sample2.wav' 
audio, sample_rate, _, _ = vf.read_wav(file_path)
text = vf.speech_to_text(audio, sample_rate)
print(text)

