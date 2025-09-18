
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json


@csrf_exempt
def cadastrar(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON invalido"}, status=400)

        username = dados.get("username")
        password = dados.get("password")
        email = dados.get("email")

        if not username or not password:
            return JsonResponse({"erro": "Username e password são obrigatorios"}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"erro": "Username e password são obrigátorios"}, status=400)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({"mensagem": "Usuário criado com sucesso!", "username": user.username})
    
    return JsonResponse({"mensagem": "Use POST para cadastrar usuários"}, status=400)


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "Json inválido"}, status=400)
        
        username = dados.get("username")
        password = dados.get("password")

        if not username or not password:
            return JsonResponse({"erro": "Username e password são obrigátorios"}, status=400)
        
        user = authenticate(username=username, password=password)
        if user:
            return JsonResponse({"mensagem": "Login bem-sucedido", "username":user.username})
        else:
            return JsonResponse({"erro": "Usuário ou senha incorretos"})
        
    return JsonResponse({"mensagem": "use POST para fazer login"}, status=405)
        
    
    