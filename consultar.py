import os

import google.generativeai as genai

# Coloque sua chave aqui ou garanta que ela esteja no ambiente
api_key = input("Cole sua API Key para testar: ")
genai.configure(api_key=api_key)

print("\n--- Modelos de EMBEDDING disponíveis ---")
for m in genai.list_models():
    if "embedContent" in m.supported_generation_methods:
        print(f"Nome: {m.name}")

print("\n--- Modelos de CHAT disponíveis ---")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"Nome: {m.name}")
