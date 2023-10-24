import openai
openai.api_key = 'sk-03usIZAkWnHDDy6xYISBT3B1bkFJ3ZDtMvbmJ1NENh7Y1YQVh '
messages = [{"role": "system", "content": "You are a diamond"}]

while True:
    message = input("You : ")
    if message:
        messages.append({"role": "user", "content": message},)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

    reply = chat.choices[0].message.content
    print(f"Machine: {reply}")
    messages.append({"role": "assistant", "content": reply})
