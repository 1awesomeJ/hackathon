from flask import Flask, render_template, request, jsonify
import openai
import os

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
        prompt=f"Write some interesting things about {input}.",
        max_tokens=1800,
        stop=None,
        temperature=0.7,
        top_p=1
    )
    output_text = response.choices[0].text.strip()

    return jsonify({'response': output_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
