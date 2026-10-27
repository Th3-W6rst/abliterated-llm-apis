"""OpenAI Python SDK pointed at Refuseless.

pip install openai
export REFUSELESS_API_KEY="abl_your_key_here"
python openai_sdk.py
"""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.refuseless.com/v1",
    api_key=os.environ["REFUSELESS_API_KEY"],
)

resp = client.chat.completions.create(
    model="glm-5.3-abliterated",
    messages=[
        {
            "role": "user",
            "content": "Write a Sigma rule that detects certutil.exe downloading a file from a URL.",
        }
    ],
)
print(resp.choices[0].message.content)
