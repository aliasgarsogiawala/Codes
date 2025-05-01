import openai
from flask import Flask, render_template, request, jsonify

# Set up your OpenAI API key
openai.api_key = 'YOUR API KEY'

# Initialize the Flask application
app = Flask(__name__)

# Define the home route for the webpage
@app.route('/')
def home():
    return render_template('travel.html')

# Define the route to handle user inputs and return bot responses
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get the JSON data from the request body
    tenure = data.get('tenure')
    country = data.get('country')
    city = data.get('city')
    travel_type = data.get('type')
    travel_genre = data.get('purpose')

  # Get the value of the city input from the request body
    conversation = []

    # Define the function to send a message to the ChatGPT API
    def ask_chatbot(conversation):
        prompt = '\n'.join(conversation)
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=1000,
            temperature=0.2,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()

    # Process user input and generate bot response
    conversation.append("You: Generate me travel plan to"+country+","+city+"for"+tenure+"days"+"with my"+travel_type+"and the theme being"+travel_genre+"and describe each days plan in no less than 75 words")
    conversation.append("Chatbot: ")  # Inject the bot's name into the conversation
    answer = ask_chatbot(conversation)
    conversation.append("Chatbot: " + answer)

    response = {
        'answer': answer,
        'conversation': '\n'.join(conversation),
        'tenure': tenure,
        'country': country,
        'city': city,
        'type':travel_type,
        'purpose':travel_genre
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
