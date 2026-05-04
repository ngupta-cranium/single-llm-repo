import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Question"}],
)
print(message)
