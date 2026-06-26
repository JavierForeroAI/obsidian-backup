#!/usr/bin/env python3
"""
Script de ingesta de clientes a GHL
Genera: contactos, tags, custom fields, scoring
"""

import json
import requests
from datetime import datetime

# Cargar datos
with open("/Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/_data/clientes_consolidado.json", "r") as f:
    clientes = json.load(f)

GHL_TOKEN = "{GHL_API_TOKEN}"  # ← REEMPLAZAR CON TOKEN REAL
GHL_LOCATION = "{GHL_LOCATION_ID}"  # ← REEMPLAZAR

BASE_URL = "https://rest.gohighlevel.com/v1"

def crear_contacto(cliente):
    """Crea contacto en GHL"""
    payload = {
        "firstName": cliente["nombre"].split()[0],
        "lastName": " ".join(cliente["nombre"].split()[1:]) if len(cliente["nombre"].split()) > 1 else "",
        "email": cliente["email"],
        "phone": cliente["telefono"],
        "address": cliente["direccion"],
        "customFields": {
            "ciudad": cliente["ciudad"],
            "procedimiento": cliente["procedimiento"],
            "valor_lifetime": str(cliente["valor"]),
            "tipo_cliente": cliente["tipo_transaccion"],
        },
        "tags": [
            f"cliente-{cliente['ciudad'].lower()}",
            f"{cliente['tipo_transaccion'].lower()}",
            "clientes-innovart"
        ]
    }
    
    # Realizar petición
    headers = {"Authorization": f"Bearer {GHL_TOKEN}"}
    response = requests.post(
        f"{BASE_URL}/contacts/",
        json=payload,
        headers=headers
    )
    
    return response.json()

# Procesamiento
print(f"Procesando {len(clientes)} contactos...")
for idx, cliente in enumerate(clientes):
    try:
        resultado = crear_contacto(cliente)
        if idx % 100 == 0:
            print(f"  {idx}/{len(clientes)}...")
    except Exception as e:
        print(f"  ❌ Error en {cliente['nombre']}: {e}")

print("✅ Ingesta completada")
