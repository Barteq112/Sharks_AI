
import os
from openai import AzureOpenAI

os.environ["AZURE_OPENAI_API_KEY"] = "647fa5db0d0945b3a9b2bc70c8be6a94"
api_version = "2023-07-01-preview"
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint="https://team3-hacaton.openai.azure.com/",
)

def text_to_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="ada"
    ).data[0].embedding
    return response

