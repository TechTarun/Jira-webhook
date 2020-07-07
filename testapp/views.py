from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        response = request.body
        print(response)
    else:
        print("Wrong method")
    return HttpResponse("<html><body>This is webhook test</body></html>")