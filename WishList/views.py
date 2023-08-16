from django.http import JsonResponse
from django.contrib.auth.models import User
from passlib.hash import argon2
from django.http import HttpResponse
import json

def get_token_api(request):
  # CSRFトークン取得
  csrf_token = request.META.get('CSRF_COOKIE')
  print("CSRF Token:", csrf_token)
  return HttpResponse("CSRF Token printed in terminal")

def create_user_api(request):
  if request.method == "POST" :
    data = json.loads(request.body)
  
    username = data.get("username")
    email = data.get("email")
    password = argon2.hash(data.get("password"))
    
    try:
      user = User.objects.create_user(username, email, password)
      
      # dataを使って新しいユーザーを作成
      return JsonResponse({"message": "User created"}, status = 201)
    except Exception as e:
      error_message = str(e)
      print("Error:", error_message)
      return JsonResponse({"message": "Error during registration", "error": str(e)}, status = 400)
  else:
    return JsonResponse({"message": "Invalid method"}, status = 405)