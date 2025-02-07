from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

# Create a Flask app
app = Flask(__name__)

# Reverse the LANGUAGES dictionary to map language names to codes
lang_names_to_codes = {v: k for k, v in LANGUAGES.items()}

@app.route('/')
def home():
    # Render the HTML page for the translation app
    return render_template('index.html', languages=list(LANGUAGES.values()))

@app.route('/translate', methods=['POST'])
def translate_text():
    source_language_name = request.form['source_language']
    target_language_name = request.form['target_language']
    text_to_translate = request.form['text_to_translate']

    # Convert language names to language codes
    source_language = lang_names_to_codes.get(source_language_name)
    target_language = lang_names_to_codes.get(target_language_name)

    if not text_to_translate:
        return jsonify({"error": "Please enter text to translate."})

    try:
        translator = Translator()
        translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
        return jsonify({"translated_text": translation.text})
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
