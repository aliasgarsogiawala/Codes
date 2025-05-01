import openai
from flask import Flask, render_template, request, jsonify

# Set up your OpenAI API key
openai.api_key = 'YOUR API KEY'

# Initialize the Flask application
app = Flask(__name__)

# Define the home route for the webpage
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle user inputs and return bot responses
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    conversation = request.json['conversation'].split('\n')

    # Define the function to send a message to the ChatGPT API
    def ask_chatbot(conversation):
        prompt = '\n'.join(conversation)
        response = openai.Completion.create(
            engine='gpt-3.5-turbo-0613',
            prompt=prompt,
            max_tokens=1000,
            temperature=0.2,
            n=1,
            stop=None  
        )
        return response.choices[0].text.strip()

    # Process user input and generate bot response
    if user_input.strip() == "":
        answer = "Please enter a valid input"
    if user_input=="What number is my romanian friend thinking between 1 to 10":
        answer="Let me think....my guess is 2"
    elif user_input.lower()=="who made u" or user_input.lower()=="who made u?" or user_input.lower()=="who made you?" or user_input.lower()=="who made you":
        answer="I was made by Aliasgar Sogiawala"
    elif user_input.lower() == "quit":
        answer = "Goodbye Nigga!"
    else:
        conversation.append("You: " + user_input)
        conversation.append("Chatbot: ")  # Inject the bot's name into the conversation
        answer = ask_chatbot(conversation)
        conversation.append("Chatbot: " + answer)

    response = {
        'answer': answer,
        'conversation': '\n'.join(conversation)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
