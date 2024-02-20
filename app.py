from flask import Flask, jsonify, request
from helpers import extract_keywords, query, searchYT
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/",)
def index():
    return jsonify('Welcome to Frontida'), 200

@app.route("/generateText", methods=["POST"])
def generate():
    if request.method == 'POST':
        input_text = str(request.form['text'])
        response, statusCode = query(input_text)

        ## Parse the response content as JSON
        if statusCode == 200:
            keywords = extract_keywords(input_text)
            youtubeLinks = searchYT(', '.join(keywords))
            return jsonify({"generated_text": response,"keywords":keywords, "youtubeLink": youtubeLinks}), statusCode
        else:
            return jsonify({"unexpected error": response}), statusCode
    
if __name__ == "__main__":
    app.run(debug=False)
