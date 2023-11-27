from django.shortcuts import render
from .google_bard import get_response
from django.http import JsonResponse

def index(request):
    return render(request, "index.html")


def google_bard_response(request):
    response = get_response(request.GET.get('prompt'))
    return JsonResponse({'message': response})