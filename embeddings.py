
import os
from openai import AzureOpenAI

os.environ["AZURE_OPENAI_API_KEY"] = "APIKEY"
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

