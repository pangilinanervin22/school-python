import openai
openai.api_key = "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"
messages = [{"role": "system", "content": "You are a diamond"}]

while True:
    message = input("You : ")
    if message:
        messages.append({"role": "user", "content": message},)
        chat = openai.ChatCompletion.create(
            model="gpt-4", messages=messages)

    reply = chat.choices[0].message.content
    print(f"Machine: {reply}")
    messages.append({"role": "assistant", "content": reply})
