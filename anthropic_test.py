import anthropic
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="deepseek-v4-flash",
        max_tokens=1000,
        system="You are a helpful assistant.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Hi, how are you?"
                    }
                ]
            }
        ]
    )
    print(message.content)
