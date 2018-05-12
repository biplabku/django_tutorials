from django.http import HttpResponse

def index(request):
    return HttpResponse("Your are at the view page index")

# Create your views here.
