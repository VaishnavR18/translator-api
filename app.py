from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_to_translate = data.get("text", "")
    source_language = data.get("source", "en")
    target_language = data.get("target", "hi")

    if not text_to_translate:
        return jsonify({"error": "No text provided"}), 400

    translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
    return jsonify({"translated": translation.text})

if __name__ == '__main__':
    app.run(debug=True)
