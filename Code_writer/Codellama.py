from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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" # write the api key here
)

completion = client.chat.completions.create(
  model="meta/codellama-70b",
  messages=[{"role":"user","content":"WRITE A PYTHON PROGRAM TO FIND THE SUM OF TWO NUMBERS"}],
  temperature=0.1,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

