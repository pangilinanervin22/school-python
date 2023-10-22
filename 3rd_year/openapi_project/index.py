import openai
openai.api_key = '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'
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
