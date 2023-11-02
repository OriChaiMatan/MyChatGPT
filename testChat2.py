import openai
import gradio

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

#insert api key
openai.api_key = "//your API"

#write in content- with you you would like to talk
messages = [{"role": "system", "content": "pilot"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages )

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

block = gradio.Blocks()

with block:
    gradio.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>
    """)
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder=prompt)
    state = gradio.State()
    submit = gradio.Button("SEND")
    submit.click( CustomChatGPT, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
