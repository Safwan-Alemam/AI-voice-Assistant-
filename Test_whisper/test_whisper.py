import whisper
import cohere
from gtts import gTTS


model = whisper.load_model("base")
result = model.transcribe("MyVoice.mp3")
input_text = result["text"]
print("Transcribed text: ", input_text)


co = cohere.Client('lJcxqnhGdCRHekrOWqS2eaAjArq2AsJNNvUpYC3H')
response = co.chat(message=input_text, model='command')
output_text = response.text
print("cohere Response: ", output_text)



tts = gTTS(output_text, lang='en')
tts.save("output_response.mp3")
print("Audio saved as output_response.mp3")