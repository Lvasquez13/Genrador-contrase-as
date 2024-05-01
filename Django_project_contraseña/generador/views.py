from django.shortcuts import render
import secrets
import string

def home(request):
    return render(request, 'home.html')

def generatedPassword(request):
    length = int(request.GET.get('length', 12))
    uppercase = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')

    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special:
        characters += '!@#$%^&*(){}[]'
    if numbers:
        characters += string.digits

    generated_password = ''.join(secrets.choice(characters) for _ in range(length))

    return render(request, 'password.html', {'password': generated_password})

