# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "user", "content": "What is my name?"}
    ]
)

print(response['choices'][0]['message'].content)