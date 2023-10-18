from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin

from ai import *

app = Flask(__name__)
CORS(app)

# vars
examples = parse_file_for_examples("examples.txt")

 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# request: {
#   user_message: string
# }
@app.route("/api/chat", methods=["POST"])
# @cross_origin(origins=["http://localhost:3000/"])
def hello_chat():
    # get request data, and then input text from data
    # print("hello")
    print("USER: " + request.json["user_message"])

    data = request.json
    input_text = data["user_message"]

    # get response
    response = get_response(input_text, examples)
    print("RESPONSE: " + response)

    # make http response using make_response
    status_code = 200

    http_response = make_response({"response": response}, status_code)
    return http_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
