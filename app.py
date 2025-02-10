from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import time
from gevent import monkey

monkey.patch_all()  # Enables async processing

app = Flask(__name__)

# Language mapping
languages = {
    "english": "en",
    "hindi": "hi",
    "bengali": "bn",
    "urdu": "ur",
    "punjabi": "pa"
}

@app.route('/')
def home():
    return render_template('index.html', languages=languages.keys())

@app.route('/translate', methods=['GET'])
def translate_text():
    start_time = time.time()

    # Get query parameters
    source_language = request.args.get('source_language', 'english').lower()
    target_language = request.args.get('target_language', 'hindi').lower()
    text_to_translate = request.args.get('text_to_translate', '')

    if not text_to_translate:
        return render_template('index.html', languages=languages.keys(), error="Please enter text.")

    if source_language not in languages or target_language not in languages:
        return render_template('index.html', languages=languages.keys(), error="Invalid language.")

    try:
        # Translation using deep_translator
        translated_text = GoogleTranslator(source=languages[source_language], target=languages[target_language]).translate(text_to_translate)

        # Convert translated text to speech
        audio_file = "static/translated_audio.mp3"
        gTTS(text=translated_text, lang=languages[target_language]).save(audio_file)

        end_time = time.time()
        print(f"Processing time: {end_time - start_time} seconds")

        return render_template('index.html', languages=languages.keys(), translated_text=translated_text, audio_file=audio_file)

    except Exception as e:
        return render_template('index.html', languages=languages.keys(), error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
