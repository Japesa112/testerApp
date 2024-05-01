from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)

# Load the Whisper model
model = whisper.load_model("base")

@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    data = request.json
    audio_url = data.get('audio_url')
    if audio_url:
        try:
            # Transcribe the audio
            result = model.transcribe(audio_url)
            transcribed_text = result.get('text')
            return jsonify({'transcription': transcribed_text})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'No audio URL provided'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)

