from openai import OpenAI

from constants import API_KEY, BASE_URL, MODEL

prompt = "What's the formula for energy?"
messages = [{"role": "user", "content": prompt}]

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


response = client.chat.completions.create(
    model=MODEL, messages=messages, temperature=0.0
)

print(response.usage.completion_tokens)
