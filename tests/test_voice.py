import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import numpy as np
from unittest.mock import patch, Mock
from src.voice import Voice
from src import ASSETS
import wave
import base64

def test_to_bytes():
    vf = Voice()
    data = np.array([1, 2, 3, 4], dtype=np.int16)
    result = vf.to_bytes(data)
    expected = data.tobytes()

    assert result == expected

def test_read_wav():
    path = ASSETS + "/test.wav"
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(np.array([0, 32767, -32768], dtype=np.int16).tobytes())
    
    vf = Voice()
    audio, sample_rate, duration, n_frames = vf.read_wav(path)

    assert sample_rate == 44100
    assert duration == pytest.approx(3 / 44100, rel=1e-2)
    assert n_frames == 3
    assert np.array_equal(audio, np.array([0, 32767, -32768], dtype=np.int16))


@patch('voice.req.post')
def test_speech_to_text(mock_post):
    vf = Voice()

    mock_resp = Mock()
    mock_resp.json.return_value = {"text": "Hello world"}
    mock_post.return_value = mock_resp

    audio = np.array([0, 32767, -32768], dtype=np.int16)
    sampling_rate = 44100

    result = vf.speech_to_text(audio, sampling_rate, "eng", False)

    mock_post.assert_called_once()
    assert result == {"text": "Hello world"}

    _, kwargs = mock_post.call_args
    data = kwargs['data']
    assert data['sampling_rate'] == sampling_rate
    assert data['target_lang'] == "eng"
    assert data['pii_mask'] == "false"
    assert base64.b64decode(data['audio']) == vf.to_bytes(audio)
