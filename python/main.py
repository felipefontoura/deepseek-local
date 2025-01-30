from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="xxx",  # required, but unused
)

response = client.chat.completions.create(
    model="deepseek-r1:7b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The LA Dodgers won in 2020."},
        {"role": "user", "content": "Where was it played?"},
    ],
    stream=True,
)
# Print the streaming response as it arrives
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # just add a newline at the end
