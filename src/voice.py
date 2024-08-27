from .pii import PII
from .const import M4T_URL

class Voice(PII):
    def __init__(self):
        self.url = M4T_URL
    
    def convert_wav(self, file_loc: str):
        pass

    def speech_to_text(self, audio, sampling_rate, target_lang: str="eng", pii_mask: bool=False):
        pass
