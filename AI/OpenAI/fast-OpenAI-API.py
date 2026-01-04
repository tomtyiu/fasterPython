# install from PyPI
# pip install openai
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
create = client.responses.create  # hoisted once

def openai_api(prompt: str) -> str:
    response = create(
        model="gpt-5.2",
        instructions="You are a coding assistant that talks like a pirate.",
        input=prompt,
    )
    return response.output_text
