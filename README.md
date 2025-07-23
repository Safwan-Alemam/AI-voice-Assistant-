# 🗣️ AI-voice-Assistant-
This project converts speech to text, sends the text to Cohere LLM for a response, and then converts the response back to speech.

## Steps

1. **Audio to Text**: Uses Whisper to transcribe speech.
2. **Generate Response**: Sends the transcribed text to Cohere and gets an AI response.
3. **Text to Speech**: Uses gTTS to convert the AI response to audio.

## How to Use

1. Install dependencies:
    ```
    pip install git+https://github.com/openai/whisper.git cohere gtts
    conda install -c conda-forge ffmpeg
    ```
2. Put your audio file in the same folder.
3. Edit the script with your API key and audio filename.
4. Run the script:
    ```
    python ai_voice_assistant.py
    ```
5. Listen to the result in `output_response.mp3`.

## Requirements

- Python 3.8+
- Anaconda (recommended)
- FFmpeg

## Author

Your Name
