import os
import openai

PROMPT = "A programmer teaching programming online in front of computer"

openai.api_key = "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" # replace with your actual API key

#Method 1
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])

#Use following Method to store picture locally
# https://realpython.com/generate-images-with-dalle-openai-api/