# Przykładowy kod do dodawania elementów do wektorowej bazy danych
from pymilvus import MilvusClient
import embeddings
import opis
import podzial

# Dane dostępowe do serwera
CLUSTER_ENDPOINT = "ENDPOINT"
TOKEN = "TOKEN"


# Inicjalizacja klienta
client = MilvusClient(
    uri=CLUSTER_ENDPOINT,
    token=TOKEN
)



# Funkcja dodająca dane do bazy



def add_to_database(text_to_add,name):
    data = {
        'name': name,
        'text': text_to_add,
        'vector': embeddings.text_to_embedding(text_to_add),
        'opis': opis.summarize_function(text_to_add)
    }
    res = client.insert(
        collection_name="AI",
        data=[data]
    )
    return res
functions_in_project = podzial.find_functions_in_django_project(r'C:\Users\mati\Desktop\Django-School-Management-System-master1')
print(len(functions_in_project))
for function_name, function_code in functions_in_project:
    print(function_name)
    add_to_database(function_code, function_name)
