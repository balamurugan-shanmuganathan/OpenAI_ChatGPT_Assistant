import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Chat GPT"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "OpenAI ChatGPT Assistant")

demo.launch(share=True)
