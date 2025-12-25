from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
# Load the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize conversation history
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    # This serves the HTML file from the 'templates' folder
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    # Parse the incoming JSON data
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']
    
    global conversation_history
    if len(conversation_history) > 6:
        conversation_history = conversation_history[-6:]
        
    # ------------------------------------------

    # Create conversation history string
    history = "\n".join(conversation_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response (Added max_length for safety)
    outputs = model.generate(**inputs, max_length=60)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    
    app.run(port=5000)