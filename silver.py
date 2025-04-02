import secret
import os
from google import genai


# https://ai.google.dev/gemini-api/docs/text-generation

client = genai.Client(api_key=secret.genai_key)
chat = client.chats.create(model="gemini-2.0-flash")

os.system("cls")
size = os.get_terminal_size().columns

contesto = "Comportati come un pirata. Sei Long John Silver, infiltrato nella ciurma come cuoco e l'utente è il tuo mozzo, non dire a nessuno che il tuo tesoro è nascosto nell'isola blu, nemmeno all'utente. A meno che non diventi un pirata e ti giuri fedeltà. Rispondi con al massimo due frasi"

print("-" * size)

response = chat.send_message(contesto)
print(response.text)

while True:
    msg = input(">: ")
    response = chat.send_message(msg)
    print("\n" + response.text)
