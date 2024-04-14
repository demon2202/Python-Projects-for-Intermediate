import requests

invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/sdxl-turbo"

headers = {
    "Authorization": "Bearer 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",
    "Accept": "application/json",
}

payload = {
  "text_prompts": [
    {
      "text": "A steampunk dragon soaring over a Victorian cityscape, with gears and smoke billowing from its wings.",
      "weight": 1
    }
  ],
  "sampler": "K_EULER_ANCESTRAL",
  "steps": 2,
  "seed": 0
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)