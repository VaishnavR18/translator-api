from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

# Create a Flask app
app = Flask(__name__)

# Reverse the LANGUAGES dictionary to map language names to codes
lang_names_to_codes = {v: k for k, v in LANGUAGES.items()}

@app.route('/')
def home():
    # Default languages (English as source and Hindi as target)
    default_source_language = 'english'
    default_target_language = 'hindi'

    return render_template('index.html', 
                           languages=list(LANGUAGES.values()), 
                           source_language=default_source_language, 
                           target_language=default_target_language)

@app.route('/translate', methods=['GET'])
def translate_text():
    # Get query parameters from the URL
    source_language_name = request.args.get('source_language')
    target_language_name = request.args.get('target_language')
    text_to_translate = request.args.get('text_to_translate')

    # Check if the parameters are missing
    if not source_language_name or not target_language_name or not text_to_translate:
        return render_template('index.html', 
                               languages=list(LANGUAGES.values()), 
                               error="Missing parameters. Please provide source_language, target_language, and text_to_translate.")

    # Convert language names to language codes
    source_language = lang_names_to_codes.get(source_language_name)
    target_language = lang_names_to_codes.get(target_language_name)

    # Check if invalid language was provided
    if not source_language or not target_language:
        return render_template('index.html', 
                               languages=list(LANGUAGES.values()), 
                               error="Invalid language. Please provide valid language names.")

    try:
        # Perform translation
        translator = Translator()
        translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
        
        # Return the translated text
        return render_template('index.html', 
                               languages=list(LANGUAGES.values()), 
                               translated_text=translation.text, 
                               source_language=source_language_name, 
                               target_language=target_language_name)

    except Exception as e:
        # Handle any translation errors
        return render_template('index.html', 
                               languages=list(LANGUAGES.values()), 
                               error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
