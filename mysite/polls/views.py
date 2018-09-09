from django.http import HttpResponse

def index(request):
    return HttpResponse("Hurray! I remembered the code. You are seeing the result :)")