import os

# Intenta obtener la clave API de OpenAI desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

print(f"La clave API de OpenAI es: {openai_api_key}")

if openai_api_key is None:
    print("La clave API de OpenAI no está definida.")
else:
    print("La clave API de OpenAI está definida correctamente.")
