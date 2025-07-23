# 🗣️ AI-voice-Assistant-
This project converts speech to text, sends the text to Cohere LLM for a response, and then converts the response back to speech.

---

## 🚀 Features

- **Speech-to-Text:** Converts audio (e.g., MyVoice.mp3) to text using [OpenAI Whisper](https://github.com/openai/whisper).
- **AI Response:** Sends the transcribed text to [Cohere LLM](https://cohere.com/) and gets a short, smart reply.
- **Text-to-Speech:** Converts the AI's response to speech using [gTTS](https://pypi.org/project/gTTS/), supporting different accents.

---

## 🛠️ Setup & Installation

1. **Clone or Download the Project Folder.**

2. **Set Up a Conda Environment (Recommended):**
   ```
   conda create -n ai-voice python=3.9
   conda activate ai-voice
   ```

3. **Install Required Packages:**
   ```
   pip install git+https://github.com/openai/whisper.git cohere gtts
   conda install -c conda-forge ffmpeg
   ```

4. **Add Your Audio File:**
   - Place your audio file (for example, `MyVoice.mp3`) in the same folder as the script.

5. **Get Your Cohere API Key:**
   - Register at https://dashboard.cohere.com/api-keys and copy your API key.
   - Paste it into the script where it says `cohere.Client('YOUR_COHERE_API_KEY')`.

---

## 🏃 How to Run

1. **Edit** `test_whisper.py`:
   - Update with your audio file name and Cohere API key if needed.
   - Adjust `lang='en-uk'` in gTTS to another accent if you want.
2. **Run the script:**
   ```
   python test_whisper.py
   ```
3. **Listen to the result:**  
   The response will be saved as `output_response.mp3`.

---

## 📝 Example Code

```python
import whisper
import cohere
from gtts import gTTS

# 1. Transcribe audio with Whisper
model = whisper.load_model("base")
result = model.transcribe("MyVoice.mp3", language='en')
input_text = result["text"]
input_text = input_text.replace("Safoan", "Safwan")
print("Transcribed text: ", input_text)

# 2. Generate short response from Cohere
short_prompt = "Reply in no more than 2 sentences: " + input_text
co = cohere.Client('YOUR_COHERE_API_KEY')
response = co.chat(message=input_text, model='command')
output_text = response.text
print("Cohere Response: ", output_text)

# 3. Convert to speech with gTTS (e.g., 'en-uk' for UK English)
tts = gTTS(output_text, lang='en-uk')
tts.save("output_response.mp3")
print("Audio saved as output_response.mp3")
```

---

## ❓ FAQ

**Q:** How do I use a different voice/accent?  
**A:** Change `lang='en-uk'` to another accent in gTTS, such as `'en'` (US), `'en-au'` (Australian), or `'ar'` (Arabic).

**Q:** Can I use a different audio file?  
**A:** Yes! Just change `"MyVoice.mp3"` in the script.

**Q:** Can I use a microphone directly?  
**A:** Yes, with a few changes. Ask for a sample script if you need this feature.

---

## 📋 Requirements

- Python 3.8 or newer
- Anaconda (recommended, but optional)
- FFmpeg

---

## 👤 Author

Safwan alemam
