from transformers import AutoProcessor, SeamlessM4Tv2Model
from .pii import PII

class Voice(PII):
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
        self.model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")
        self.pii = PII()
    
    def __convert(self, audio, target_lang: str="eng", enable_gpu: bool=False) -> str:
        output_tokens = self.model.generate(**audio, tgt_lang="fra", generate_speech=False)
        return self.processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)

    def speech_to_text(self, audio, target_lang: str="eng", pii_mask: bool=False):
        audio_input = self.processor(audios=audio, return_tensors="pt")
        translated_text = self.__convert(audio_input)
        #return self.pii.mask(target=["Person"])
        return translated_text
