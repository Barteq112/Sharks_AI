from openai import AzureOpenAI
import os

api_version = "2023-07-01-preview"
os.environ["AZURE_OPENAI_API_KEY"] = "647fa5db0d0945b3a9b2bc70c8be6a94"
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint="https://team3-hacaton.openai.azure.com/",
)


def summarize_function(funkcja):
    completion = client.chat.completions.create(
        model="gpt4-turbo",
        messages=[
            {
                "role": "system",
                "content": "Jesteś kompilatorem kodu, sporządź krótkie podsumowanie funkcji. Wypełnij pola: Nazwa Funkcji, Input, Output, Krótki opis",
            },
            {
                "role": "user",
                "content": funkcja,
            },
        ],
    )

    return completion.choices[0].message.content


