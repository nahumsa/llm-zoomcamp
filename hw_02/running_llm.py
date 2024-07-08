from openai import OpenAI

from constants import API_KEY, BASE_URL, MODEL

messages = [{"role": "user", "content": "10 * 10"}]

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

response = client.chat.completions.create(model=MODEL, messages=messages)
print(response.choices[0].message.content)
