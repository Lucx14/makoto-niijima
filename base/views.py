from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello this will be my articles index page")
