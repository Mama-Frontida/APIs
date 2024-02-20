from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/generate-text", methods=["POST"])
def generate():
    # Validate the request body as JSON
#   //  data = request.get_json()
    text = "Hello, how are you?"

    # Make a POST request to the chatbot API's endpoint
    url = "https://api-inference.huggingface.co/models/Njambi-M/gpt2-finetuned"
    response = requests.post(url, headers={"Authorization": "Bearer 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"},
                             json={"inputs": text})

    ## Parse the response content as JSON
    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text'].split('\n')[1].replace('[a]', '').replace('[q]', '').strip()
        # Return the response text as the output
        return jsonify({"generated_text": generated_text})
    else:
         return jsonify({"unexpected error": response.text}), response.status_code
    
if __name__ == "__main__":
    app.run(debug=False)