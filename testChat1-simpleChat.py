import openai

#insert api key

openai.api_key = "" //your API

#write your answer in: "content"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": " what is bible?"}])
print(completion.choices[0].message.content)
