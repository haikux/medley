from src import PDF, Voice, PII, PPTX


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

vf = Voice()
file_path = '/Users/haikux/Documents/projects/medley/assets/audio/sample2.wav' 
audio, sample_rate, _, _ = vf.read_wav(file_path)
text = vf.speech_to_text(audio, sample_rate)
print(text)
"""

"""
# Load and parse PPTX
"""
pptx = '/Users/haikux/Documents/projects/medley/assets/pptx/sample.pptx'
px = PPTX(pptx)
res = px.get_metadata()
#res = px.read_page(page=1, save_images=False)
print(res)


