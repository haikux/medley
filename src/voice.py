from .pii import PII
from .const import M4T_URL
import numpy as np
import wave
import json
import base64
import requests as req

class Voice(PII):
    def __init__(self):
        self.url = M4T_URL
    
    def to_bytes(self, data: np.array) -> bytes:
        return data.tobytes()

    
    def read_wav(self, file_loc: str):
        with wave.open(file_loc, 'rb') as wav_file:
            sample_rate = wav_file.getframerate()
            n_frames = wav_file.getnframes()
            duration = n_frames / sample_rate
            audio_data = wav_file.readframes(n_frames)
        audio = np.frombuffer(audio_data, dtype=np.int16)
        return audio, sample_rate, duration, n_frames

    def speech_to_text(self, audio, sampling_rate, target_lang: str="eng", pii_mask: bool=False):
        headers = {"Content-Type": "application/json"}
        audio_bytes = self.to_bytes(audio)
        data = {'audio': base64.b64encode(audio_bytes).decode("utf-8"), 
                'sampling_rate': sampling_rate, 'target_lang': 'eng', 'pii_mask': 'false'}
        resp = None
        try:
            resp = req.post(self.url, headers=headers, data=data)
        except Exception as e:
            print(str(e))
        return resp.json()
