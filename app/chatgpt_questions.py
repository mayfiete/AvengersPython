import requests

# Set up API request
url = "https://api.openai.com/v1/engines/davinci-codex/completions"
prompt = input("Who is your favorite superhero? ")
data = {
    "prompt": prompt,
    "max_tokens": 1024,
    "n": 1,
    "stop": "\n",
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "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",
}

# Send API request
response = requests.post(url, json=data, headers=headers)

# Check response status code
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

# Write response to text file
with open("response.txt", "w") as f:
    f.write(response.json()["choices"][0]["text"])
    print("Response written to response.txt")
