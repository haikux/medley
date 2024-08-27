import numpy as np
import torch
from transformers import AutoProcessor, SeamlessM4Tv2Model

class Voice:
    def __init__(self, device: str = "cpu"):
        self.device = torch.device(device)
        self.processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
        self.model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large").to(self.device)
    
    def __convert(self, audio, target_lang: str = "eng", enable_gpu: bool = False) -> str:
        output_tokens = self.model.generate(**audio, tgt_lang=target_lang, generate_speech=False)
        return self.processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

    def speech_to_text(self, audio, sampling_rate, target_lang: str = "eng", pii_mask: bool = False):
        # Ensure audio is normalized and in float32 format
        if isinstance(audio, np.ndarray) and audio.dtype == np.int16:
            audio = audio.astype(np.float32) / 32768.0
        
        audio_input = self.processor(audios=audio, sampling_rate=sampling_rate, return_tensors="pt").to(self.device)
        translated_text = self.__convert(audio_input, target_lang=target_lang)
        
        return translated_text