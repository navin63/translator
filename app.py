from flask import Flask, render_template, request

from googletrans import Translator

app = Flask(__name__)

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        translation_direction = request.form['direction']

        if translation_direction == 'en_to_hi':
            hindi_translation = translate_to_hindi(text)
            return render_template('index.html', original_text=text, hindi_translation=hindi_translation, translation_direction=translation_direction)

        elif translation_direction == 'hi_to_en':
            english_translation = translate_to_english(text)
            return render_template('index.html', original_text=text, english_translation=english_translation, translation_direction=translation_direction)

    return render_template('index.html')


    

if __name__ == '__main__':
    app.run(debug=True)
