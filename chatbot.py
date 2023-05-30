# Import necessary libraries
import openai

# Set up OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define function for generating chatbot response
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

# Define function for user interaction
def chat():
    print("ChatGPT: Hello! I'm ChatGPT, a rule-free chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ")
        prompt = f"User: {user_input}\nChatGPT:"

        response = generate_response(prompt)
        print("ChatGPT:", response)

        if user_input.lower() == "bye":
            print("ChatGPT: Goodbye! Have a great day!")
            break

# Start the chat
chat()
