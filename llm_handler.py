import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(email_content):
    prompt = f"Classify and rewrite the following email in a more professional tone:\n\n{email_content}"
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an email rewriting and classification assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return chat_completion.choices[0].message.content