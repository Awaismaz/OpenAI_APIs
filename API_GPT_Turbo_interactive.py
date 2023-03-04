# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"

messages=[]

prompt=input('User: ')

while prompt:
  prompt_obj= {"role": "user", "content": f"{prompt}"}
  messages.append(prompt_obj)

  response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  response_content=response['choices'][0]['message']["content"].strip()
  print(f"Assistant: {response_content}")
  response_obj={"role": "assistant", "content": f"{response_content}"}
  messages.append(response_obj)

  prompt=input('User: ')

