from flask import Flask, request
import numpy as np
from voice import Voice
from io import BytesIO
import base64

app = Flask(__name__)
voice = Voice()

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio = request.form['audio']
    sampling_rate = request.form['sampling_rate']
    target_lang = request.form.get('target_lang', 'eng')
    pii_mask = request.form.get('pii_mask', 'false').lower() == 'true'
    print(audio[:20])
    audio = base64.b64decode(audio)
    audio_data = np.frombuffer(audio, dtype=np.int16)
    text = voice.speech_to_text(audio_data, int(sampling_rate), target_lang, pii_mask)
    return text

if __name__ == '__main__':
    app.run()