from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import CustomUserCreation
import json
from django.contrib.auth import authenticate, login

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = CustomUserCreation(data)
            
            if form.is_valid():
                user = form.save()  # Save user instance to database
                return JsonResponse({"Message": "User successfully registered"}, status=201)
            else:
                # Return form errors in a cleaner way
                return JsonResponse({"error": form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    
    return JsonResponse({'message': 'Send a POST request with user data'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('Name')
            password = data.get('number')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({'message': 'Send a POST request with user data'}, status=405)


        

    