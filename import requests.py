import openai
import requests
import json

# Set up the API endpoint and parameters
url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}
data = {
    'prompt': 'Write a function that takes an input string and returns the length of the string',
    'max_tokens': 128  # Increase max_tokens value
}

# Send the HTTP POST request to the OpenAI API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse the response and print the completed text
json_response = json.loads(response.text)
#print(json_response)
completed_text = json_response['choices'][0]['text']
print(completed_text)