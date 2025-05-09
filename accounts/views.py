from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import CustomUserCreation
import json

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
