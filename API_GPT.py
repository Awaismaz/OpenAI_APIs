import openai

openai.api_key = "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"


response= openai.Completion.create(
  engine="text-davinci-003",
  prompt="Write a Copy to sell cowboy hat",
  max_tokens=200
)

print(response["choices"][0].text)