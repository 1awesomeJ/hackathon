from flask import Flask, render_template, request, jsonify
import openai
import os
import requests
from pydub import AudioSegment

app = Flask(__name__)
app.config['DEBUG'] = True

openai_key = os.getenv('OPENAI_API_KEY')
if not openai_key:
    raise ValueError('Missing OPENAI API key')

openai.api_key = openai_key

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/symptom-checker')
def symptom_checker():
    input = request.args.get('input')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write detailed informattion about these symptoms, mention some of the ailments they could be indicative of, and list possible first-aid remedies: {input}.",
        max_tokens=1800,
        stop=None,
        temperature=0.7,
        top_p=1
    )
    output_text = response.choices[0].text.strip()

    return jsonify({'response': output_text})

@app.route('/to_whisper', methods=['POST'])
def to_whisper():
    url="https://whisper.lablab.ai/asr"
    payload={}
    audio_data = request.files['audio_file']
    #files=[ ('audio_file',('test.mp3',open('test.mp3','rb'),'audio/mpeg')) ]
    files=[ ('audio_file',('test.mp3',audio_data,'audio/mpeg')) ]
    response_w = requests.request("POST", url, data=payload, files=files)
    input = response_w.json()["text"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write detailed informattion about these symptoms, mention some of the ailments they could be indicative of, and list possible first-aid remedies: {input}.",
        max_tokens=1800,
        stop=None,
        temperature=0.7,
        top_p=1
    )
    output_text = response.choices[0].text.strip()

    return jsonify({'response': output_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0',
             port=3000,
             ssl_context=('cert.pem', 'key.pem')
             )
