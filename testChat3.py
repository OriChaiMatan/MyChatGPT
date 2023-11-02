import os
import openai
import gradio

prompt = "The following is a conversation with an AI Pope. The Pope is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nThe Pope: I am an AI created by OpenAI. How can I bless you today?\nHuman: "

#insert api key
openai.api_key = "" /your API

#write in content- with you you would like to talk
messages = [{"role": "system", "content": "you are the pope"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create( model = "gpt-3.5-turbo", messages = messages)

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = CustomChatGPT(inp)
    history.append((input, output))
    return history, history

block = gradio.Blocks()

with block:
    gradio.Markdown("""<h1><center>Chat with the pope</center></h1>
    """)
    chatbot = gradio.Chatbot()
    mes = gradio.Textbox(placeholder=prompt)
    state = gradio.State()
    submit = gradio.Button("SEND FOR BLESSING")
    submit.click( chatgpt_clone, inputs=[mes, state], outputs=[chatbot, state]) 

block.launch(debug = True)
