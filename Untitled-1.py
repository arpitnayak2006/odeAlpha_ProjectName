def chatbot_response(user_input):
    """
    Function to return predefined responses based on user input.
    """
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"
    elif user_input in ["how are you", "how's it going"]:
        return "I'm fine, thanks for asking!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you rephrase?"

# Chatbot interaction loop
print("Simple Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)