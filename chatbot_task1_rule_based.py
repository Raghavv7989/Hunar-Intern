def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "weather" in user_input:
        return "The weather is sunny and clear."
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

while True:
    query = input("You: ")
    if "bye" in query.lower():
        print("Bot:", chatbot_response(query))
        break
    print("Bot:", chatbot_response(query))
