from transformers import VitsModel, AutoTokenizer, pipeline
import torch

class MMSModel:
    def __init__(self):
        self.model = VitsModel.from_pretrained("facebook/mms-tts-eng")
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")
    
    def convert_to_speech(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            output = self.model(**inputs).waveform
            return output