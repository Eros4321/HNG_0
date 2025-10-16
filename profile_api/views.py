from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import datetime, timezone

@api_view(['GET'])
def me(request):
    try:
        cat_response = requests.get('https://catfact.ninja/fact', timeout=5)
        cat_response.raise_for_status()
        fact = cat_response.json().get('fact', 'No cat fact available right now.')
    except Exception as e:
        fact = f"Could not fetch cat fact: {str(e)}"

    data = {
        "status": "success",
        "user": {
            "email": "BenjaminOwase@gmail.com",
            "name": "Benjamin Eromosele Odion-Owase",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }
    return Response(data)

