from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/highlight', methods=['POST'])
def highlight_word():
    text = request.form['text']
    word = request.form['word']
    highlighted = re.sub(rf'\b({re.escape(word)})\b', r'*\1*', text, flags=re.IGNORECASE)
    return jsonify({'highlighted': highlighted})

if __name__ == '__main__':
    app.run(debug=True)
